import tweepy
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()



configure()
auth = tweepy.OAuthHandler(consumer_key = os.getenv("api_key"), consumer_secret = os.getenv("api_key_secret"))
auth.set_access_token(os.getenv("access_token"), os.getenv("access_token_secret"))
api = tweepy.API(auth)


#user = api.me()
#print(user.followers_count)

# to save time & better learning: do the new documentation and also install new tweety version and use its latest documentation!


"""
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

#def a limit handler

#generate bot: follow back users

#like pyquant news tweets

"""