"""
Retrieve tweets, embeddings, and persist in the database.
"""
import basilica
import tweepy
from .models import DB, Tweet, User


TWITTER_AUTH = tweepy.OAuthHandler(getenv('TWITTER_CONSUMER_KEY'),
                                  getenv('TWITTER_CONSUMER_SECRET'))
TWITTER_AUTH.set_access_token(getenv('TWITTER_ACCESS_TOKEN'),
                             getenv('TWITTER_ACCESS_TOKEN_SECRET'))
TWITTER = tweepy.API(TWITTER_AUTH)
BASILICA = basilica.Connection(getenv('BASILICA_KEY'))

def add_or_update_user(username):
    """
    Add or update a user and their tweets. 
    Return an error if not a Twitter user.
    """
    