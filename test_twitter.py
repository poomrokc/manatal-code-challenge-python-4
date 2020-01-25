"""
Tests for get_followers function
Author: Poompatai Puntitpong
"""

import twitter

def test_twitter_1():
    assert(twitter.get_followers('https://twitter.com/KMbappe') >= 3800000)

def test_twitter_2():
    assert(twitter.get_followers('https://twitter.com/KMbappe?randomstring') >= 3800000)

def test_twitter_3():
    assert(twitter.get_followers(' https://twitter.com/KMbappe/?randomstring') >= 3800000)

def test_twitter_4():
    assert(twitter.get_followers('https://twitter.com/Facebook') >= 13000000)

def test_twitter_5():
    assert(twitter.get_followers('https://twitter.com/instagram') >= 36000000)

def test_twitter_6():
    assert(twitter.get_followers('https://twitter.com/Snapchat') >= 2000000)