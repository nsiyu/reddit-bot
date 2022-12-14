from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import praw
import json
import pandas as pd
import random
from selenium.webdriver.common.keys import Keys

from undetected_chromedriver import Chrome


subreddit_list = ['csMajors']

reddit_read_only = praw.Reddit(client_id = "fy4lfFdgNJIfwCKqg3Xi1A", client_secret = 'BPOLUIxWJZW8oKtlUQkXNaP6-qZPQg', user_agent = "Weak")
reddit = praw.Reddit(client_id ='fy4lfFdgNJIfwCKqg3Xi1A', 
                     client_secret ='BPOLUIxWJZW8oKtlUQkXNaP6-qZPQg', 
                     user_agent ='Weak', 
                     username ='StanfordStudent112', 
                     password ='Temppass!')

def get_relevant_text(subreddit):
    dict = []
    subreddit = reddit_read_only.subreddit(subreddit)
    for post in subreddit.hot(limit=3):
        dict.append(post.selftext)
    return dict

def comment_on_post(sub, message):
    subreddit = reddit.subreddit(sub)
    for post in subreddit.hot(limit=3):
        if hasattr(post, "body"):
            post.reply(message)

def parse_text(dict):
    dict.pop(0)
    dict.pop(0)
    n_names = ["{}\n".format(i) for i in dict]
    for i in range(len(n_names)):
        for char in n_names[i]:
            if char in " []\\:*🫡~ ":
                n_names[i].replace(char,' ')
    return n_names

def post_to_subreddit(sub, title, text):
    selftext = text
    reddit.subreddit(sub).submit(title, selftext = selftext)

def main():
    #input handling
    # client_id = input("Enter Client_id: ")
    # client_secret = input_("Enter Client_secret") 
    # user_agent = input("Enter User_Secret")
    # username = input("Enter username")
    # password = input("Enter Password")

    for subreddit in subreddit_list:
        #get relevant text
        dict = parse_text(get_relevant_text(subreddit))
        body = ""

        for str in dict:
            body += str
        
        for char in body:
            if char in "[]\\:*🫡~":
                body = body.replace(char, '')

        browser = Chrome()
        browser.get("https://chat.openai.com/")
        time.sleep(3)
        browser.find_element('xpath','//*[@id="__next"]/div/div/div[4]/button[1]').click()
        time.sleep(3)
        browser.find_element('xpath', '/html/body/main/section/div/div/div/div[3]/form[1]/button/span[2]').click()
        time.sleep(3)
        element = browser.find_element('xpath', '//*[@id="identifierId"]')
        time.sleep(3)
        element.send_keys('willy200335')
        time.sleep(3)
        browser.find_element('xpath', '//*[@id="identifierNext"]/div/button/span').click()
        time.sleep(3)
        password = browser.find_element('xpath', '//*[@id="password"]/div[1]/div/div[1]/input')
        time.sleep(3)
        password.send_keys('weiho920305')
        time.sleep(3)
        browser.find_element('xpath', '//*[@id="passwordNext"]/div/button/span').click()
        time.sleep(3)


        browser.find_element('xpath','//*[@id="headlessui-dialog-panel-:r1:"]/div[2]/div[4]/button').click()
        time.sleep(3)
        browser.find_element('xpath','//*[@id="headlessui-dialog-panel-:r1:"]/div[2]/div[4]/button[2]').click()
        time.sleep(3)
        browser.find_element('xpath','//*[@id="headlessui-dialog-panel-:r1:"]/div[2]/div[4]/button[2]').click()
        time.sleep(3)

        type = browser.find_element('xpath','//*[@id="__next"]/div/div[1]/main/div[2]/form/div/div[2]/textarea')
        type.send_keys("Please respond to this post: ")
        type.send_keys(body)
        type.send_keys(Keys.RETURN)
        time.sleep(20)
        

        comment = (browser.find_element(By.XPATH ,'//*[@id="__next"]/div/div[1]/main/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/p').text)
        print(comment)
        time.sleep(3)
        
        browser.close()
        #get title and body from chatGPT
        

        
        #comment_on_post(subreddit, comment)

        #create new reddit post (subreddit, testing, helloworld)
        #post_to_subreddit(subreddit, title , body)
        time.sleep(10)


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
# element = driver.find_element('xpath','//*[@id="__next"]/div/div/div[4]/button[1]')
# element.click()

# time.sleep(5)