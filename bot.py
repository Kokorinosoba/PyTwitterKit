import sys
import json
from requests_oauthlib import OAuth1Session
from setting import API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET


class Twitter():
    def __init__(self):
        self.requests = OAuth1Session(API_KEY,
                                      API_SECRET_KEY,
                                      ACCESS_TOKEN,
                                      ACCESS_TOKEN_SECRET)

    def print_tweet(self, result):
        if result.status_code == 200:
            tweets = json.loads(result.text)
            print("-" * 60)
            if type(tweets) == dict:
                tweets = tweets["statuses"]
            for tweet in tweets:
                print(f'{tweet["user"]["name"]} @{tweet["user"]["screen_name"]} ID:{tweet["id_str"]}\n{tweet["full_text"]}')
                print("-" * 60)

    def get(self, url, params):
        result = self.requests.get(url, params=params)
        print(sys._getframe(1).f_code.co_name, result)
        self.print_tweet(result)
        return result

    # --- Accounts and users ---
    # Create and manage lists

    # Follow, Search, and get users

    # Manage account setting and profile

    # Mute, block and report users

    # Subscribe to account activity

    # --- Tweets ---
    # Curate a collection of Tweets

    # Filter realtime tweets

    # Get Tweet timelines
    def GET_statuses_home_timeline(self, count=None, since_id=None, max_id=None, trim_user=None, exclude_replies=None, include_entities=None):
        url = "https://api.twitter.com/1.1/statuses/home_timeline.json?tweet_mode=extended"
        params = {"count": count,
                  "since_id": since_id,
                  "max_id": max_id,
                  "trim_user": trim_user,
                  "exclude_replies": exclude_replies,
                  "include_entities": include_entities}
        return self.get(url, params)

    def GET_statuses_mentions_timeline(self, count=None, since_id=None, max_id=None, trim_user=None, include_entities=None):
        url = "https://api.twitter.com/1.1/statuses/mentions_timeline.json?tweet_mode=extended"
        params = {"count": count,
                  "since_id": since_id,
                  "max_id": max_id,
                  "trim_user": trim_user,
                  "include_entities": include_entities}
        return self.get(url, params)

    def GET_statuses_user_timeline(self, user_id=None, screen_name=None, since_id=None, count=None, max_id=None, trim_user=None, exclude_replies=None, include_rts=None):
        url = "https://api.twitter.com/1.1/statuses/user_timeline.json?tweet_mode=extended"
        params = {"user_id": user_id,
                  "screen_name": screen_name,
                  "since_id": since_id,
                  "count": count,
                  "max_id": max_id,
                  "trim_user": trim_user,
                  "exclude_replies": exclude_replies,
                  "include_rts": include_rts}
        return self.get(url, params)

    # Post, retrieve and engage with Tweets
    def POST_statuses_destroy(self, id):
        url = f"https://api.twitter.com/1.1/statuses/destroy/{id}.json"
        params = {"id": id}
        result = self.requests.post(url, params=params)
        print("statuses_destroy", result)

    def POST_statuses_update(self, status):
        url = "https://api.twitter.com/1.1/statuses/update.json"
        param = {"status": status}
        result = self.requests.post(url, params=param)
        print("statuses_update", result)

    # Search Tweets
    def GET_search_tweets(self, search_word, count=10, result_type="recent"):
        url = "https://api.twitter.com/1.1/search/tweets.json?tweet_mode=extended"
        param = {"q": search_word, "count": count, "lang": "ja", "result_type": result_type}
        result = self.requests.get(url, params=param)
        print("search_tweets", result)
        self.print_tweet(result)
        return result
