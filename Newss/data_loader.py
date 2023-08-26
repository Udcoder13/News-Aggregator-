import os
import sys
import django

# Set the Django project's path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(BASE_DIR, '..'))  # Adjust '..' if needed to point to your Django project's root directory

# Initialize Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newsa.settings')  # Replace 'your_project_name' with your actual project name
django.setup()
import requests

from Newss import models


def get_news():
    url= "https://newsapi.org/v2/top-headlines?country=in&apiKey=a4afc29713c246649d96d08b5e5eb70d"


    data=requests.get(url)
    if data.status_code==200:
       print(data.json())
       return data.json()
    else:
       print('failed')
 #     return None
 
def save_data():
    data=get_news()
    if data and "articles" in data:
       articles=data["articles"]

       for a in articles:
          item=models.News(
             title=a['title'],
             description=a['description'],
             content=a['content'],
             url=a['url'],
             image=a['urlToImage'],
             publishedAt=a['publishedAt'],
             source='News',
          )
          item.save()
     
        
save_data()