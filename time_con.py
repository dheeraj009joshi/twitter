import datetime

str="Wed Mar 09 13:57:30 +0000 2022"
f=datetime.datetime.strptime(str, '%a %b %d %H:%M:%S +0000 %Y').strftime('%d/%m/%Y')

print(f)