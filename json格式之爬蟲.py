import requests
import json
x = requests.get("https://www.googleapis.com/books/v1/volumes?q=python")    #get data from this website
dic = json.loads(x.text)
for item in dic['items']:
    print('title:',item['volumeInfo']['title']) #get book title
    print('subtitle:', item['volumeInfo'].get('subtitle','None'))   #get book subtitle, if no then place 'None'
    print('====================')
