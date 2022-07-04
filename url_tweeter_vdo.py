import requests
h= {'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAI3ZZwEAAAAALlqr33MJOeFcQnoyoB8z%2Fj65jps%3Dra5UXOI6Keztn0gQoTGhmIAf6FPlwPU2tydCXjQ3ZyH48Id4MZ'}

d=requests.request("GET","https://api.twitter.com/1.1/statuses/show.json?id=<3_1500954445848457222>&include_entities=true",headers=h)

print(d.content)




