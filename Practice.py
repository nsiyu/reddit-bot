from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import praw
import json
import pandas as pd

reddit_read_only = praw.Reddit(client_id="xmAsnL6OKfcL6I20P0txag",         
                               client_secret="dWL6xW-kue5LoolcziQDdu6kqx-baw",    
                               user_agent="nsiyu")

def get_relevant_text(subreddit):
    dict = []
    subreddit = reddit_read_only.subreddit(subreddit)
    for post in subreddit.hot(limit=10):
        dict.append(post.selftext)
    return dict

def parse_text(dict):
    dict.pop(0)
    dict.pop(0)
    n_names = ["{}\n".format(i) for i in dict]
    for i in range(len(n_names)):
        for char in n_names[i]:
            if char in " [] ":
                n_names[1].replace(char,' ')
    return n_names

def post_to_subreddit(subreddit, title, text):
    subreddit.post_to_subreddit(title, text)

def main():
    #get relevant text
    dict = parse_text(get_relevant_text("csmajors"))
    
    #copy into chatGPT
    
    #create new reddit post (subreddit, testing, helloworld)
    post_to_subreddit("csmajors", "testing", "hello world")

if __name__ == "__main__":
    main()











# driver = webdriver.Chrome(r"./driver/chromedriver")

# chrome_options = webdriver.ChromeOptions()
# prefs = {"profile.default_content_setting_values.notifications" : 2}
# chrome_options.add_experimental_option("prefs",prefs)
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.get("https://www.reddit.com/r/csmajors/")
  
# # Maximize the window and let code stall 
# # for 10s to properly maximise the window.
# driver.maximize_window()
# time.sleep(5)
  
# # Obtain button by link text and click.
# element = driver.find_element('xpath','//*[@id="t3_zkaa17"]/div[3]/div[3]/a/div/div/div[1]')
# element.click()

# time.sleep(5)