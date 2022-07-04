import datetime
import json
import re
import csv
import pandas as pd
import requests

url = 'http://life.cubesservices.com/api/v1/Videos/Insert'
commenturl = 'http://life.cubesservices.com/api/v1/Comment/Insert'
userUrl = 'http://life.cubesservices.com/api/v1/Users/InstagramUser'
  
def insertUser(userData):

    biography =str(userData["description"])
    reqjsn = {
        'Name': userData["screen_name"],
        'FullName': str(userData["name"]),
        'MigratedProfileImage': str(userData["profile_image_url_https"]).replace("'",""),
        'InstagramVerified': '',
        'InstagramFollowerCount': userData["followers_count"],
        'InstagramFollowingCount': userData["friends_count"],
        'UserDescription': biography.replace("\n", " ").replace("\t", " "),
        'ExternalUrl': '',
        'InstagramBusiness': '',
        'Email':'',
        'InstagramPk': userData['id'],
        'MediaCount': userData['statuses_count'],
        "Age": 0,
        "Sex": "instagramuser",
        "Race": "instagramuser",
        "Interests": "instagramuser",
        "NativePlace": "instagramuser",
    }
    
    print()
    print()
    print()
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    res = requests.post(userUrl, data=reqjsn, headers=headers,verify=False)
    print('time', 'message', 'inserted users :- ' + res.text)
    print()
    print()
    print()
    return res.text


def postComment(post, HASHTAG, userId):
    jsn = {"Hashtag1": '', "Hashtag2": '',
           "Hashtag3": '', "Hashtag4": '', "Hashtag5": ''}

    caption = re.sub("([#@])\\w+", "", post["full_text"] or "")
    print(userId)
    reqjsn = {
        'InLocation': True,
        'Text': caption.replace("\n", " ").replace("\t", " "),
        'MigratedImage': post["extended_entities"]['media'][0]['media_url_https'],
        'Latitude': latitude,
        'Longitude': longitude,
        'BatchName': str(batch),
        'userId': userId,
        'Emoji': DefaultEmoji,
        "Hashtag": '#'+str(HASHTAG),
        "Hashtag1": jsn["Hashtag1"],
        "Hashtag2": jsn["Hashtag2"],
        "Hashtag3": jsn["Hashtag3"],
        "Hashtag4": jsn["Hashtag4"],
        "Hashtag5": jsn["Hashtag5"],
        "MigratedDate":datetime.datetime.strptime(post["created_at"], '%a %b %d %H:%M:%S +0000 %Y').strftime('%d %B %Y'),
        "Hide": True,
        "CityId": str(CityId),
        
        "LikeCount":post['favorite_count'],

    }


    print(reqjsn)
    res = requests.post(commenturl, json=reqjsn)
    print('time', 'message',  'inserted comment :- ' + res.text)


def lookpost(post, HASHTAG, userId):
    vidurl = post["extended_entities"]['media'][0]['video_info']['variants'][0]['url']
    jsn = {"Hashtag1": '', "Hashtag2": '',
           "Hashtag3": '', "Hashtag4": '', "Hashtag5": ''}
   
    caption = re.sub("([#@])\\w+", "", post["full_text"] or "")
    
    print(userId)

    reqjsn = {
        'InLocation': True,
        'VideoDescription': caption.replace("\n", " ").replace("\t", " "),
        'MigratedVideoURL': vidurl,
        'MigratedThumbnailURL': post["extended_entities"]['media'][0]['media_url_https'],
        'Latitude': latitude,
        'Longitude': longitude,
        'BatchName': batch,
        'userId': userId,
        'Emoji': DefaultEmoji,
        "Hashtag": '#'+str(HASHTAG),
        "Hashtag1": jsn["Hashtag1"],
        "Hashtag2": jsn["Hashtag2"],
        "Hashtag3": jsn["Hashtag3"],
        "Hashtag4": jsn["Hashtag4"],
        "Hashtag5": jsn["Hashtag5"],
        "MigratedDate": datetime.datetime.strptime(post["created_at"], '%a %b %d %H:%M:%S +0000 %Y').strftime('%d %B %Y'),
        "Hide": True,
        "CityId": str(CityId),
        "LikeCount":post['favorite_count'],

    }
    print(reqjsn)

    res = requests.post(url, json=reqjsn,verify=False)
    print('time', 'message',  'inserted video :- ' + res.text)






h= {'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAI3ZZwEAAAAALlqr33MJOeFcQnoyoB8z%2Fj65jps%3Dra5UXOI6Keztn0gQoTGhmIAf6FPlwPU2tydCXjQ3ZyH48Id4MZ'}

querrys="Kharkiv"
batch='Battles'
DefaultEmoji ='1F4A3'  
CityId= ''  
latitude=49.994507
longitude=36.145742
next_tok=None
for it in range(0,10):
    query_params = {'query': f"{querrys} -is:retweet has:media",
                    'max_results':100,
                    'expansions': 'author_id,in_reply_to_user_id,geo.place_id,attachments.media_keys',
                    'tweet.fields': 'attachments,id,text,author_id,in_reply_to_user_id,geo,conversation_id,created_at,lang,public_metrics,referenced_tweets,reply_settings,source',
                    "media.fields":'media_key,type,duration_ms,height,preview_image_url,public_metrics,width,alt_text',
                    'user.fields': 'id,name,username,created_at,description,public_metrics,verified',
                    'place.fields': 'full_name,id,country,country_code,geo,name,place_type',
                    'next_token': next_tok}

    response = requests.request("GET", "https://api.twitter.com/2/tweets/search/recent", headers = h, params = query_params)
    print("Endpoint Response Code: " + str(response.status_code))
    response=json.dumps(response.json(), indent=4, sort_keys=True)
    response=(json.loads(response))
    # print(response)
    next_tok=response['meta']['next_token']
    print(next_tok)
    for  i in response['data']:

        Tid=i['id']
        main_data=requests.request("GET",f"https://api.twitter.com/1.1/statuses/show.json?id={Tid}&tweet_mode=extended",headers=h)
        js=main_data.json()

        try:
            if js['extended_entities']['media'][0]['type']=="video":
                print("video")
                userId=insertUser(js['user'])
                lookpost(js,HASHTAG=querrys,userId=userId)

            elif js['extended_entities']['media'][0]['type']=="photo":
                print("photo")
                userId=insertUser(js['user'])
                postComment(js,HASHTAG=querrys,userId=userId)
        except:
            pass     

        
        
        