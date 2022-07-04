
import datetime
import json
import re
import time
import requests

url = 'http://life.cubesservices.com/api/v1/Videos/Insert'
commenturl = 'http://life.cubesservices.com/api/v1/Comment/Insert'
userUrl = 'http://life.cubesservices.com/api/v1/Users/InstagramUser'
querrys="cats"
batch='Battles'
DefaultEmoji ='1F4A3'  
CityId= ''  
latitude=50.401699
longitude=30.252512
def insertUser(userData):

    biography =str(userData["description"])
    reqjsn = {
        'Name': userData["screen_name"],
        'FullName': str(userData["name"]),
        'MigratedProfileImage': userData["profile_image_url_https"],
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
def get_rules(h, bearer_token):
    response = requests.get(
        "https://api.twitter.com/2/tweets/search/stream/rules", headers=h
    )
    if response.status_code != 200:
        raise Exception(
            "Cannot get rules (HTTP {}): {}".format(response.status_code, response.text)
        )
    print(json.dumps(response.json()))
    return response.json()

def delete_all_rules(headers, bearer_token, rules):
    if rules is None or "data" not in rules:
        return None

    ids = list(map(lambda rule: rule["id"], rules["data"]))
    payload = {"delete": {"ids": ids}}
    response = requests.post(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        headers=headers,
        json=payload
    )
    if response.status_code != 200:
        raise Exception(
            "Cannot delete rules (HTTP {}): {}".format(
                response.status_code, response.text
            )
        )
    print(json.dumps(response.json()))
    
    
    
def set_rules(h,rule, delete, bearer_token):
    # You can adjust the rules if needed
    sample_rules = [rule]
    payload = {"add": sample_rules}
    response = requests.post(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        headers=h,
        json=payload,
    )
    if response.status_code != 201:
        raise Exception(
            "Cannot add rules (HTTP {}): {}".format(response.status_code, response.text)
        )
    print(json.dumps(response.json()))
    
    
    
    
    
    
    
query_params = {
                    'expansions': 'author_id,in_reply_to_user_id,geo.place_id,attachments.media_keys',
                    'tweet.fields': 'attachments,id,text,author_id,in_reply_to_user_id,geo,conversation_id,created_at,lang,public_metrics,referenced_tweets,reply_settings,source',
                    "media.fields":'media_key,type,duration_ms,height,preview_image_url,public_metrics,width,alt_text',
                    'user.fields': 'id,name,username,created_at,description,public_metrics,verified',
                    'place.fields': 'full_name,id,country,country_code,geo,name,place_type',
                    'max_id': {}}

response = requests.request("GET", "https://api.twitter.com/2/tweets/search/stream", headers = h, params = query_params,stream=True
                            )
print("Endpoint Response Code: " + str(response.status_code))

def get_stream(h, set, bearer_token):

    response = requests.get(
        "https://api.twitter.com/2/tweets/search/stream", headers=h,params=query_params, stream=True,
    )
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Cannot get stream (HTTP {}): {}".format(
                response.status_code, response.text
            )
        )
    print("done")
    for response_line in response.iter_lines():
        
        if response_line:
            tweet=json.loads(response_line)
            # print(tweet)
            Tid=tweet['data']['id']
            main_data=requests.request("GET",f"https://api.twitter.com/1.1/statuses/show.json?id={Tid}&tweet_mode=extended",headers=h)
            js=main_data.json()

            try:
                if js['extended_entities']['media'][0]['type']=="video":
                    print("video")
                    userId=insertUser(js['user'])
                    lookpost(js,HASHTAG=batch,userId=userId)

                elif js['extended_entities']['media'][0]['type']=="photo":
                    print("photo")
                    userId=insertUser(js['user'])
                    postComment(js,HASHTAG=batch,userId=userId)
            except Exception as e :
                print(e)
                pass     

# def main():
#     bearer_token = h
#     headers = h
#     rule={"value": "Kyiv has:media lang:en -is:retweet", "tag": "war in "}
#     rules = get_rules(headers, bearer_token)
#     delete = delete_all_rules(headers, bearer_token, rules)
#     set = set_rules(headers,rule, delete, bearer_token)
#     get_stream(headers, set, bearer_token)
def main():
    
    bearer_token = h
    headers = h
    timeout=0
    while True:
        get_stream(headers, set, bearer_token)
        time.sleep(5)
        timeout+=5
    
if __name__ == "__main__":
    main()            
            