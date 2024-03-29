import tweepy, os
from dotenv import load_dotenv
load_dotenv()

consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_KEY_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

mail = os.getenv("EMAIL_LOGIN")
passw = os.getenv("EMAIL_PASSWORD")

try:
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    print("API authorization: success!")

except:
    print("API authorization: FAILURE!")