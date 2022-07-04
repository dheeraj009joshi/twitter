from logging import exception
from xml.etree.ElementInclude import include
from numpy import result_type
import tweepy
import json
from config import *

api_key=API_Key
api_key_secret=API_Key_Secret
access_token=Access_Token
acs_tkn_secret=Access_Token_Secret
auth=tweepy.OAuth1UserHandler(api_key,api_key_secret)
auth.set_access_token(access_token,acs_tkn_secret)

api=tweepy.API(auth,wait_on_rate_limit=True)

try:
    api.verify_credentials()
    print("Authentication OK")
except Exception as e:
    print(e)
    print("Error during authentication")
    
    
available_loc = api.search_tweets(q=("modi je ")+"-filter:retweets",lan="eng",count=10,result_type='mixed',include_entitle=True,tweet_mode="extended",locals="usa")
# print(available_loc)
for i in available_loc:
    json_str = json.dumps(available_loc[0]._json)
    print(type(json_str))
    json_str=json.loads(json_str)
    m=api.update_status(status="pollhole.com",in_reply_to_status_id=json_str['id'],auto_populate_reply_metadata=True)
    print(m )
    print(json_str)
