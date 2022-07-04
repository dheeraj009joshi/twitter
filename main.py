import  json
import pytz
from datetime import datetime,timedelta
from time import strptime
from  instagrapi import  Client
cl=Client()
user_id=cl.user_id_from_username("pranikadhakshu")
med=cl.user_medias(user_id,5)
print(med)