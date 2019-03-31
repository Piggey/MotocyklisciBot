import tweepy
from secrets import *

#create an OAuthHandler instance
#Twitter requires all requests to use OAuth for authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 

auth.set_access_token(access_token, access_secret)

#Construct the API instance
api = tweepy.API(auth) # create an API object