from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'A Reddit bot that automatically reads and responds to posts on Reddit. It uses the Reddit API to access the posts and OpenAI\'s ChatGPT to understand the content of the posts and generate appropriate responses.'
LONG_DESCRIPTION = 'A package that allows to read posts on Reddit in real time and generates appropriate responses to the posts.'

# Setting up
setup(
    name="reddit-bot",
    version=VERSION,
    author="nsiyu",
    author_email="nsiyuhuang@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['selenium', 'time', 'undetected_chromedriver', 'praw'],
    keywords=['python', 'reddit', 'bot', 'automated'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
