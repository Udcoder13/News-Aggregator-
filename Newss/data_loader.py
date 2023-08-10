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
    apikey = "f894d7ab6caa85386f38bf6b0bb39f1a"
    url = f"https://gnews.io/api/v4/search?q=example&lang=en&country=us&max=10&apikey={apikey}"
    data=requests.get(url)
    print("Status Code:" ,data.status_code)
    print("Response Content:", data.content) # Add this line to see the HTTP status code
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
             image=a['image'],
             publishedAt=a['publishedAt'],
          )
          item.save()
save_data()