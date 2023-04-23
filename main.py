#INSTALL SELENIUM BEFORE RUNNING THIS CODE
#pip3 install selenium
# import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import getpass
from selenium.common.exceptions import NoSuchElementException

# helper function
def elementHasClass(element, active):
    print(element.get_attribute("class").split(" "))
    return active in element.get_attribute("class").split(" ")
 

#IF USING A RASPBERRY PI, FIRST INSTALL THIS OPTIMIZED CHROME DRIVER
#sudo apt-get install chromium-chromedriver
browser_driver = Service('/usr/lib/chromium-browser/chromedriver')
page_to_scrape = webdriver.Chrome(service=browser_driver)
# page_to_scrape.get("http://quotes.toscrape.com")
# word_to_search = input("Input the keyword to search")
word_to_search = "123"
page_to_scrape.get("https://search.bilibili.com/all?keyword="+word_to_search)

# get data 

# go to next page until there is no next page
while True:
    # scroll to the bottom
    page_to_scrape.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # wait to load
    time.sleep(2)
    # process
    videos = page_to_scrape.find_elements(By.CSS_SELECTOR, ".bili-video-card__info--tit");
    for video in videos:
      print(video.get_attribute("title"))
    next_page_button = page_to_scrape.find_elements(By.CSS_SELECTOR, "button.vui_pagenation--btn-side")[1]
    if (elementHasClass(next_page_button, "vui_button--disabled")):
      break;
    next_page_button.click()
    # wait to load
    time.sleep(2)



# searchBox = page_to_scrape.find_element(By.CLASS_NAME, "nav-search-input")
# searchBox.send_keys("厨房")
# page_to_scrape.find_element(By.CLASS_NAME, "nav-search-btn").find_element(By.CSS_SELECTOR, "path").click;
# username = page_to_scrape.find_element(By.ID, "username")
# password = page_to_scrape.find_element(By.ID, "password")
# username.send_keys("admin")
# #USING GETPASS WILL PROMPT YOU TO ENTER YOUR PASSWORD INSTEAD OF STORING
# #IT IN CODE. YOU'RE ALSO WELCOME TO USE A PYTHON KEYRING TO STORE PASSWORDS.
# my_pass = getpass.getpass()
# password.send_keys(my_pass)
# page_to_scrape.find_element(By.CSS_SELECTOR, "input.btn-primary").click()
# 
# quotes = page_to_scrape.find_elements(By.CLASS_NAME, "text")
# authors = page_to_scrape.find_elements(By.CLASS_NAME, "author")
# 
# # file = open("scraped_quotes.csv", "w")
# # writer = csv.writer(file)
# 
# writer.writerow(["QUOTES", "AUTHORS"])
# while True:
#     quotes = page_to_scrape.find_elements(By.CLASS_NAME, "text")
#     authors = page_to_scrape.find_elements(By.CLASS_NAME, "author")
#     # for quote, author in zip(quotes, authors):
#     #     print(quote.text + " - " + author.text)
#     #     writer.writerow([quote.text, author.text])
#     try:
#         page_to_scrape.find_element(By.PARTIAL_LINK_TEXT, "Next").click()
#     except NoSuchElementException:
#         break
# file.close()

