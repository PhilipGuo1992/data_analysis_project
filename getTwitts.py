import os
import tweepy
import socket
import json
import re

class TweetsListener(tweepy.StreamListener):

    def __init__(self, csoket):
        super(TweetsListener, self).__init__()
        self.client_socket = csoket

    def on_status(self, status):
        tweet = self.get_tweet(status)
        self.client_socket.send((tweet[2] + "\n").encode('utf-8'))
        return True

    def on_error(self, status_code):
        print("Status code")
        print(status_code)

    def get_tweet(self, tweet):
        text = tweet.text
        if hasattr(tweet, 'extended_tweet'):
            text = tweet.extended_tweet['full_text']
        return [str(tweet.user.id), tweet.user.screen_name, tweet.user.created_at, self.clean_str(text)]

    def clean_str(self, string):
        string = re.sub(r"\n|\t", " ", string)
        return string





if __name__ == "__main__":
    consumer_key = 'z56cu40Jq1XxntXeGKLfhNZnk'
    consumer_secret = 'NWsAOtbQ4lVGPq7xooVbE21XEeMnDuFBtdTfyZzc85Czh4wKnm'
    access_token = '1003752992171024386-lsvEB53AROSLhKGJgEchdgajkBJTIC'
    access_token_secret = 'NV7vVHJX3FrGJFm1fx7hivxKBLOfVom34gYAJeaUEklX1'

    host = "localhost"
    #port = 0

    s = socket.socket()
    s.bind((host, 0))

    #print("Listening on port: %s" % str(port))

    s.listen(5)
    c, addr = s.accept()

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    streamListener = TweetsListener(c)

    twitter_stream = tweepy.Stream(auth=api.auth, listener=streamListener, tweet_mode='extended')
    twitter_stream.filter(track=['$APPL'])
