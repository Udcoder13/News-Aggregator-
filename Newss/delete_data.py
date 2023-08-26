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

def delete_data():
    data=models.News.objects.all()
    data.delete()

delete_data()