"""
Manatal python Exercise 4: Scraping Test
Author: Poompatai Puntitpong
"""

import requests
import json

bearer_token = 'AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA'
graphQL_key = 'G6Lk7nZ6eEKd7LBBZw9MYw'
api_url = 'https://api.twitter.com/graphql/' + graphQL_key 

def clean_input(input):
    input = input.strip()
    input = input.split('?')[0]
    input = input.rstrip('/')
    return input

def get_api_username(input):
    return input.split('/')[-1].lower()

def generate_payload(username):
    payload_dict = {
        'screen_name': username,
        'withHighlightedLabel': False        
    }
    return json.dumps(payload_dict)

def send_api_request(username):
    payload = generate_payload(username)
    url = api_url + '/UserByScreenName?variables=' + payload
    headers = {'content-type': 'application/json; charset=utf-8', 'Authorization': 'Bearer ' + bearer_token}
    req = requests.get(url, headers=headers)
    if req.status_code!=200:
        raise requests.RequestException('Bearer token error or graphQL key has changed')
    return req.json()

def get_followers(input):
    input = clean_input(input)
    username = get_api_username(input)
    api_response = send_api_request(username)
    return api_response['data']['user']['legacy']['followers_count']
    

if __name__ == '__main__':
    print('URL to twitter profile:')
    follower = get_followers(input())
    print('Number of followers:',follower)
    