from requests_oauthlib import OAuth1Session
import json
from setting import API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET


class Twitter():
    def __init__(self):
        self.twitter = OAuth1Session(API_KEY,
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

    def statuses_update(self, status):
        url = "https://api.twitter.com/1.1/statuses/update.json"
        param = {"status": status}
        result = self.twitter.post(url, params=param)
        print("statuses_update", result)

    def statuses_destroy(self, id):
        url = "https://api.twitter.com/1.1/statuses/destroy/"+id+".json"
        params = {"id": id}
        result = self.twitter.post(url, params=params)
        print("statuses_destroy", result)

    def statuses_home_timeline(self, count=10):
        url = "https://api.twitter.com/1.1/statuses/home_timeline.json?tweet_mode=extended"
        param = {"count": count}
        result = self.twitter.get(url, params=param)
        print("statuses_home_timeline", result)
        self.print_tweet(result)
        return result

    def statuses_user_timeline(self, screen_name, count=10):
        url = "https://api.twitter.com/1.1/statuses/user_timeline.json?tweet_mode=extended"
        param = {"screen_name": screen_name, "count": count}
        result = self.twitter.get(url, params=param)
        print("statuses_user_timeline", result)
        self.print_tweet(result)
        return result


    def search_tweets(self, search_word, count=10, result_type="recent"):
        url = "https://api.twitter.com/1.1/search/tweets.json?tweet_mode=extended"
        param = {"q": search_word, "count": count, "lang": "ja", "result_type": result_type}
        result = self.twitter.get(url, params=param)
        print("search_tweets", result)
        self.print_tweet(result)
        return result
