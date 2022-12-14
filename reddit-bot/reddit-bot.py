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

#subreddit_list = ['csMajors']

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
    post.replace('\n', ' ')
    return post

#Creates a new post on specified subreddit
def post_to_subreddit(sub, title, text):
    selftext = text
    reddit.subreddit(sub).submit(title, selftext = selftext)

def main():
    # input handling
    c_id = input("Enter Client_id: ")
    c_s = input_("Enter Client_secret") 
    u_a = input("Enter User_Secret")
    user = input("Enter username")
    passw = input("Enter Password")
    global reddit_read_only
    global reddit
    reddit_read_only = praw.Reddit(client_id = c_id, client_secret = c_s, user_agent = u_a)
    reddit = praw.Reddit(client_id = c_id, 
                     client_secret = c_s, 
                     user_agent = u_a, 
                     username = user, 
                     password = passw)
    subreddit = reddit.subreddit("AskReddit")
    number = 0
    for post in subreddit.hot(limit=10):
        number += 1

        #Parses current post
        body = parse_text(post.title)
        print(body)        

        #Opens ChatGPT and Logs-in
        browser = Chrome()
        browser.get("https://chat.openai.com/")
        time.sleep(3)
        browser.find_element('xpath','//*[@id="__next"]/div/div/div[4]/button[1]').click()
        time.sleep(3)
        browser.find_element('xpath', '/html/body/main/section/div/div/div/div[3]/form[1]/button/span[2]').click()
        time.sleep(3)
        element = browser.find_element('xpath', '//*[@id="identifierId"]')
        time.sleep(3)
        element.send_keys('Redditbotnumber2')
        time.sleep(3)
        browser.find_element('xpath', '//*[@id="identifierNext"]/div/button/span').click()
        time.sleep(3)
        password = browser.find_element('xpath', '//*[@id="password"]/div[1]/div/div[1]/input')
        time.sleep(3)
        password.send_keys('botnumber2')
        time.sleep(3)
        browser.find_element('xpath', '//*[@id="passwordNext"]/div/button/span').click()
        time.sleep(3)
        browser.find_element('xpath','//*[@id="headlessui-dialog-panel-:r1:"]/div[2]/div[4]/button').click()
        time.sleep(3)
        browser.find_element('xpath','//*[@id="headlessui-dialog-panel-:r1:"]/div[2]/div[4]/button[2]').click()
        time.sleep(3)
        browser.find_element('xpath','//*[@id="headlessui-dialog-panel-:r1:"]/div[2]/div[4]/button[2]').click()
        time.sleep(3)

        #Types Message to Chat GPT and Retrives Response
        type = browser.find_element('xpath','//*[@id="__next"]/div/div[1]/main/div[2]/form/div/div[2]/textarea')
        type.send_keys("Please respond to this post: ")
        type.send_keys(body)
        time.sleep(5)
        type.send_keys(Keys.RETURN)
        time.sleep(25)
        comment = (browser.find_element(By.XPATH ,'//*[@id="__next"]/div/div[1]/main/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/p').text)
        time.sleep(3)
        browser.close()
        
        #Comments on Reddit Post
        if "OpenAI" in comment:
            print("Invalid Response")
            continue
        comment_on_post(post, comment, number)
        time.sleep(5)


if __name__ == "__main__":
    main()
