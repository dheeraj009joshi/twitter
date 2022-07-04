import csv
import datetime
from tkinter import *
import requests as re
from tkinter import filedialog as fd
import tkinter as tk
from tkinter import Button, ttk

url = 'http://life.cubesservices.com/api/v1/Videos/Insert'
commenturl = 'http://life.cubesservices.com/api/v1/Comment/Insert'
userUrl = 'http://life.cubesservices.com/api/v1/Users/InstagramUser'
DefaultEmoji=''
CityId=''
root = Tk()
BatchName=Variable()
DefaultEmoji=Variable()
CityId=Variable()

UserId=[]
MigratedVideoURL=[]
MigratedThumbnailURL=[]
VideoDescription=[]
Date=[]
BatchName=[]
Emoji=[]
Hashtag=[]
Address=[]
Latitude=[]
Longitude=[]
def select_ig_accounts():
    global UserId
    global MigratedVideoURL
    global MigratedThumbnailURL
    global VideoDescription
    global Date
    global BatchName
    global Emoji
    global Hashtag
    global Address
    global Latitude
    global Longitude
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        )
    with open(f"{filename}",'r',encoding="utf8") as csv_file:
        csv_reader=csv.reader(csv_file)
        next(csv_reader, None)
       
        print()
        for i in csv_reader:
            UserId.append(i[0])
            MigratedVideoURL.append(i[1])
            MigratedThumbnailURL.append(i[2])
            VideoDescription.append(i[3])
            Date.append(datetime.datetime.strptime(i[4].replace("t",''),'%m/%d/%Y'))
            BatchName.append(i[5])
            Emoji.append(i[6])
            Hashtag.append(i[7])
            Address.append(i[8])
            Latitude.append(i[9])
            Longitude.append(i[10])
            
select_ig_accounts() 
def lookpost(UserId,MigratedVideoURL,MigratedThumbnailURL,VideoDescription,Date,BatchName,Emoji,Hashtag,Address,Latitude,Longitude):
    vidurl = MigratedVideoURL
    jsn = {"Hashtag1": '', "Hashtag2": '',
           "Hashtag3": '', "Hashtag4": '', "Hashtag5": ''}
   
    # caption = re.sub("([#@])\\w+", "", VideoDescription[i] or "")
    
    reqjsn = {
        'InLocation': True,
        'VideoDescription': VideoDescription,
        'MigratedVideoURL': vidurl,
        'MigratedThumbnailURL': MigratedThumbnailURL,
        'Latitude':Latitude,
        'Longitude': Longitude,
        'BatchName': BatchName,
        'userId': UserId,
        'Emoji':Emoji,
        "Hashtag": '#'+str(Hashtag),
        "Hashtag1": jsn["Hashtag1"],
        "Hashtag2": jsn["Hashtag2"],
        "Hashtag3": jsn["Hashtag3"],
        "Hashtag4": jsn["Hashtag4"],
        "Hashtag5": jsn["Hashtag5"],
        "MigratedDate": str(Date),
        "Hide": True,
        "CityId": str(CityId.get()),
    }
  
    print(reqjsn)
    res = re.post(url, json=reqjsn,verify=False)
    print('time', 'message',  'inserted video :- ' + res.text)
        

no=len(UserId)
for i in range(0,no):
    lookpost(UserId[i],MigratedVideoURL[i],MigratedThumbnailURL[i],VideoDescription[i],Date[i],BatchName[i],Emoji[i],Hashtag[i],Address[i],Latitude[i],Longitude[1])
      










