from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from undetected_chromedriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
import time
import praw
import json
import pandas as pd
import random
import pyperclip

#subreddit_list = ['csMajors']

reddit_read_only = praw.Reddit(client_id = "LAjXfhhtrPQUDGXdxrY0Mw", client_secret = 'h9rAXbDc6FAYVx2sp8YbfI9S0YKitg', user_agent = "Weak")
reddit = praw.Reddit(client_id ='LAjXfhhtrPQUDGXdxrY0Mw', 
                     client_secret ='h9rAXbDc6FAYVx2sp8YbfI9S0YKitg', 
                     user_agent ='Weak', 
                     username ='Wangzhaojun1314', 
                     password ='willy920305')

#Gets text from n number of posts
def get_relevant_text(subreddit):
    dict = []
    subreddit = reddit_read_only.subreddit(subreddit)
    for post in subreddit.hot(limit=3):
        dict.append(post.selftext)
    return dict

#Comments on the current post
def comment_on_post(post, message, number):
    if (post.locked):
        print("invalid post")
        return
    print("post success")
    post.reply(message)
        
#Parses text into readable format
def parse_text(post):
    for char in post:
        if char in " []\\:*🫡~ ":
            post.replace(char,' ')
    return post

#Creates a new post on specified subreddit
def post_to_subreddit(sub, title, text):
    selftext = text
    reddit.subreddit(sub).submit(title, selftext = selftext)

def main():
    # input handling
    # client_id = input("Enter Client_id: ")
    # client_secret = input_("Enter Client_secret") 
    # user_agent = input("Enter User_Secret")
    # username = input("Enter username")
    # password = input("Enter Password")
    subreddit = reddit.subreddit("AskReddit")
    number = 0
    for post in subreddit.hot(limit=10):
        
        number += 1
        #Parses current post
        body = parse_text(post.selftext)
        pyperclip.copy(body)

        #Opens ChatGPT and Logs-in
        browser = Chrome()
        browser.get("https://chat.openai.com/")
        time.sleep(2)
        browser.find_element('xpath','//*[@id="__next"]/div/div/div[4]/button[1]').click()
        time.sleep(2)
        browser.find_element('xpath', '/html/body/main/section/div/div/div/div[3]/form[1]/button/span[2]').click()
        time.sleep(2)
        element = browser.find_element('xpath', '//*[@id="identifierId"]')
        time.sleep(2)
        element.send_keys('willy200335')
        time.sleep(2)
        browser.find_element('xpath', '//*[@id="identifierNext"]/div/button/span').click()
        time.sleep(2)
        password = browser.find_element('xpath', '//*[@id="password"]/div[1]/div/div[1]/input')
        time.sleep(2)
        password.send_keys('weiho920305')
        time.sleep(2)
        browser.find_element('xpath', '//*[@id="passwordNext"]/div/button/span').click()
        time.sleep(2)
        browser.find_element('xpath','//*[@id="headlessui-dialog-panel-:r1:"]/div[2]/div[4]/button').click()
        time.sleep(2)
        browser.find_element('xpath','//*[@id="headlessui-dialog-panel-:r1:"]/div[2]/div[4]/button[2]').click()
        time.sleep(2)
        browser.find_element('xpath','//*[@id="headlessui-dialog-panel-:r1:"]/div[2]/div[4]/button[2]').click()
        time.sleep(2)

        #Types Message to Chat GPT and Retrives Response
        type = browser.find_element('xpath','//*[@id="__next"]/div/div[1]/main/div[2]/form/div/div[2]/textarea')
        type.send_keys("Please respond to this post: ")
        time.sleep(2)
        type.click()
        time.sleep(2)
        pyperclip.paste()
        time.sleep(2)
        type.send_keys(Keys.RETURN)
        time.sleep(25)
        comment = (browser.find_element(By.XPATH ,'//*[@id="__next"]/div/div[1]/main/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/p').text)
        time.sleep(2)
        browser.close()
        
        #Comments on Reddit Post
        comment_on_post(post, comment, number)
        time.sleep(5)


if __name__ == "__main__":
    main()