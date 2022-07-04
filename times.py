import  json
import os
import shutil
import time as t
from instagrapi.types import Usertag
import datetime
from time import strftime, strptime
from  instagrapi import  Client
cl = None
def write_file(data, filename):
    fh = open(filename, "w")
    try:
        fh.write(json.dumps(data))
    finally:
        fh.close()
def read_file(filename):
    fh = open(filename, "r")
    return json.load(fh)
accounts={
    'pranika_dhakshu_fan':'Qwerty@123',
    #in this  username  and pass
    
}   
time =datetime.datetime.now()
houss=datetime.timedelta(hours=112)
main_time=time-houss
fan_usernames=['pranika_dhakshu_fan']#add username  here
celevraty_account=[]
map_ing={
    'pranika_dhakshu_fan':'pranikadhakshu',
    #add dict of  target and fan account 
}

caption={
    'pranika_dhakshu_fan':'this  is caption  of  @pranika_dhakshu_fan  #pranika_dhakshu_fan',
}
main_accounts=[]
# for acc in :

for name in fan_usernames:
    IG_CREDENTIAL = name
    print(name) #to show  which account  is continue  running
    cl=Client()
    try:
        cl.login(username=name,password=accounts[name]) 
        print(f'login  {name}') 
    except Exception as e :
        print(e)
        print(" Plz... check the above exception and solve it  then  try  again ")  
   
    user_id=cl.user_id_from_username(map_ing[name])
    user_short=cl.user_info_by_username(map_ing[name])
    media_start=cl.user_medias(user_id,5)
    medias=[]
    for  i in media_start:
        medias.append(i.json())
       
    name=name +"-"  
    for js in medias:
        ja=json.loads(js)
        ff=datetime.datetime.strptime(ja['taken_at'],'%Y-%m-%dT%H:%M:%S+00:00')
        if ff>main_time:
            os.mkdir(f"{name}")
            files=os.listdir(name)#this  err  is  because  i put the  same  name  of  them  folder  as  the session  name 
            all_paths=[]
            for file in files:
                if file.endswith(('.jpg', '.png', 'jpeg')):
                    all_paths.append(file)
            if ja["media_type"] == 1:
                try:
                    print("in photo")
                    cl.photo_download(ja['pk'],name)
                    files=os.listdir(name)
                    all_paths=[]
                    for file in files:

                        if file.endswith(('.jpg', '.png', 'jpeg')):
                            all_paths.append(file)
                    cl.photo_upload(f'{name}/{all_paths[0]}',caption[name.replace("-","")],usertags=[Usertag(user=user_short, x=0.5, y=0.5)])#caption yes  i am  getting that  from the  post  itself ohk  will  create  a map also
                    shutil.rmtree(name)
                except Exception as e:
                    print(e)
                    shutil.rmtree(name)
            elif ja["media_type"] == 2 and ja["product_type"] == 'feed':
                try:
                    print("in video")
                    path=cl.video_download(ja['pk'],name)
                    files=os.listdir(name)
                    all_paths=[]
                    for file in files:
                        if file.endswith(('.jpg', '.png', 'jpeg','.mp4')):
                            all_paths.append(file)
                    print(all_paths)
                    print(all_paths[0])
                    cl.clip_upload(f'{path}',caption[name.replace("-","")],usertags=[Usertag(user=user_short, x=0.5, y=0.5)])
                    print("video upload done")
                    shutil.rmtree(name)
                except Exception as e:
                    print(e)
                    # print(f"Dur to ree {e} sleeping because folder {name} is  still open will retry  after  2 min")
                    t.sleep(120)
                    shutil.rmtree(name)
                    
                    

                
            elif ja["media_type"] == 8:
                shutil.rmtree(name)
    
        else:
            print("media  is old ")
    cl.logout()
            
        
