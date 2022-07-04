import random, requests, os.path, wget, time, configparser, json, os
from PIL import Image
from instagrapi import Client
from instagrapi.types import StoryMention, StoryMedia, StoryLink, StoryHashtag


config = configparser.ConfigParser()
config.read("config.ini")


#subreddits = json.loads(config.get('data', 'subreddits'))
#reddit = "https://meme-api.herokuapp.com/gimme/"
hashtags = json.loads(config.get('data', 'hashtags'))
rand = random.choice(hashtags)
cooldown = config.getint('settings', 'time')
#hashtags_quantity = config.getint('settings', 'hashtags_selection')

username = config['account']['username']
password = config['account']['password']
image_url = f"https://source.unsplash.com/1080x1080/?{rand}"

def main():
    while True:
        description_post = f"\nAuto Upload Post\n\n\nBy: u/anandh\nPic From: r/UnSplash\nCategory: {rand}"
    #Check for repeated photo
        if os.path.isfile(f"memes/output.jpg"):
            print("\nRemoving old pic\n")
            os.remove(f"memes/output.jpg")
            #time.sleep(10)
            continue
        else:
            #print("\nNo repeated")
        #Download image
            wget.download(image_url, out="memes/output.jpg")
        
        #Upload Photo
        while True:
            medias = cl.hashtag_medias_recent_v1("kerala" , amount=10)
            for media in medias:
                    
            print("liking")
            cl.media_like(media.dict()['pk'])
            time.sleep(5)

            bot.photo_upload_to_story(f"memes/output.jpg",mentions=[StoryMention(user=comments, x=0.49892962, y=0.703125, width=0.8333333333333334, height=0.125)],)

            print(f'Done! Starting {cooldown} cooldown')

        time.sleep(cooldown)


if name == "main":
    bot = Client()
    bot.login(username, password)
    main()