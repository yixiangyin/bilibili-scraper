import secrets
import csv
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import getpass
from selenium.common.exceptions import NoSuchElementException

# helper function
def elementHasClass(element, active):
    return active in element.get_attribute("class").split(" ")
 

def main():
  if len(sys.argv)!=2 and len(sys.argv)!=3:
    print("usage: python main.py <keyword_to_search> [page_limit]")
    return
  if (len(sys.argv)==3):
    try:
      limit = int(sys.argv[2])
      if (limit <= 0):
        print("page limit must be greater than 0")
        return 

    except ValueError:
      print("page limit is not a integer")
      return
      
    page_counter = 0
  else:
    limit = page_counter - 1
  browser_driver = Service('/usr/lib/chromium-browser/chromedriver')
  page_to_scrape = webdriver.Chrome(service=browser_driver)
  word_to_search = sys.argv[1]
  secure_num = secrets.randbelow(500000)
  # go to the website and use a random number to bypass the checking
  page_to_scrape.get("https://search.bilibili.com/all?"+"vt="+str(secure_num)+"&"+"keyword="+word_to_search)
  # go to video tab
  tabs = page_to_scrape.find_elements(By.CSS_SELECTOR, "span.vui_tabs--nav-text")
  for tab in tabs:
    if tab.text == "视频":
      tab.click()
      break
  time.sleep(3)
  # go to next page until there is no next page
  while True:
      # scroll to the bottom
      page_to_scrape.execute_script("window.scrollTo(0, document.body.scrollHeight);")
      # wait to load
      time.sleep(3)
      # get all the video cards
      videos = page_to_scrape.find_elements(By.CSS_SELECTOR, ".bili-video-card__info--tit");
      file = open("scraped_data_"+sys.argv[1]+".csv", "w")
      # write name to csv
      writer = csv.writer(file)
      writer.writerow(["VIDEONAME"])
      for video in videos:
        writer.writerow([video.get_attribute("title")])
      next_page_button = page_to_scrape.find_elements(By.CSS_SELECTOR, "button.vui_pagenation--btn-side")[1]
      if (elementHasClass(next_page_button, "vui_button--disabled")):
        break;
      # go to the next page
      next_page_button.click()
      # wait to load
      time.sleep(3)
      page_counter+=1
      if (page_counter == limit):
        break
  file.close()

main()
