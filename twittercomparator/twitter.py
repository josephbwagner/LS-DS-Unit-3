"""
Retrieve tweets, embeddings, and persist in the database.
"""
import basilica
from decouple import config
import tweepy
from .models import DB, Tweet, User


TWITTER_AUTH = tweepy.OAuthHandler(config('TWITTER_CONSUMER_KEY'),
                                  config('TWITTER_CONSUMER_SECRET'))
TWITTER_AUTH.set_access_token(config('TWITTER_ACCESS_TOKEN'),
                             config('TWITTER_ACCESS_TOKEN_SECRET'))
TWITTER = tweepy.API(TWITTER_AUTH)
BASILICA = basilica.Connection(config('BASILICA_KEY'))


def add_or_update_user(username):
    """
    Add or update a user and their tweets. 
    Return an error if not a Twitter user.
    
    Parameters
    ---------------
    username (User.screen_name): Twitter identifier

    Returns
    ---------------
    None - writes to DB
    """
    try:
        twitter_user = TWITTER.get_user(username)
        tweets = twitter_user.timeline(count=200, exclude_replies=True, include_rts=False, tweet_mode='extended')
        db_user = User(id=twitter_user.id, name=twitter_user.screen_name, newest_tweet_id=tweets[0].id)

        for tweet in tweets:
            embedding = BASILICA.embed_sentence(tweet.full_text, model='twitter')
            db_tweet = Tweet(id=tweet.id, text=tweet.full_text[:500], embedding=embedding)
            DB.session.add(db_tweet)
            db_user.tweets.append(db_tweet)

        DB.session.add(db_user)
        DB.session.commit()

    except Exception as e:
        print('The following exception occured: ', e)
    