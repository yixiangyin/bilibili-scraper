# bilibili-scraper
## Team Members
This section is a list of team members, and possibly links to GitHub/GitLab/LinkedIn/personal blog pages for members.
- [Yixiang](https://github.com/yixiangyin/)
## Tool Description
The Bilibili Scraper is a web scraping tool designed to extract all the video names by keyword from the Chineses famous video website Bilibili.
With this tool, users can quickly and efficiently gather data from Bilibili without having to manually search for and record video titles.
## [demo](https://youtu.be/hf9k6s7N2vE)
## Installation
1. Make sure you have Python version 3.8 or greater installed
2. Install selenium library
- run `pip3 install selenium`
3. Download the tool's repository using the command:
- run `git clone https://github.com/yixiangyin/bilibili-scraper`
4. Move to the tool's directory 
- run `cd bilibili-scraper`

## Usage
- Inside the project directory, run `python main.py <keyword> [page limit]`
- keyword can be anything
- page limit is optional and it has to be greater than 0

## Additional Information
- Make sure you have a fast internet because if you have a slow one, for the code to work as expect, you might need to adjust waiting time longer for the browser to load the content.
Next steps:
- [ ] create a graphical user interface
- [ ] add functionality to extract user names for a given search
