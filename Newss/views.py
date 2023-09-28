from typing import Any, Optional
from django.shortcuts import render
from .models import News,comments
from. import models
import requests
from django.views.generic import ListView,TemplateView,DetailView
from. import forms
from django.shortcuts import get_object_or_404


class index(TemplateView):
      template_name = "index.html"

class NewsList(ListView):
    model = News
    template_name = "home.html"
    context_object_name='news'

class NewsDetail(DetailView):
    model = News
    template_name = "detail.html"
    context_object_name='ndetail'
    def post(self, request,**kwargs):
        comment_form= forms.CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.news = self.get_object()  # Using self.get_object() to get the news article instance
            comment.save()
            return self.get(request,**kwargs)
        else:
           return self.get(request,**kwargs)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['form'] = forms.CommentForm() 
        comments = self.object.comments.all()  # 'comments' is the related_name you defined in the News model
        context['comments'] = comments # Add the comment form to the context
        return context
    
class CategoryView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        apikey = 'a4afc29713c246649d96d08b5e5eb70d'

        category = self.kwargs.get('category','technology')
        country = self.kwargs.get('country','in')
        url= f"https://newsapi.org/v2/top-headlines?category={category}&country={country}&apiKey={apikey}"

        response=requests.get(url)
        d=response.json()
        articles=d['articles']
        context["category"]=category
        context["articles"]=articles
        context["country"]=country
        return context
     
        
    template_name = "category.html"

class CategoryDetailView(TemplateView):        
    template_name = "category_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        index = self.kwargs.get('index')
        apikey = 'a4afc29713c246649d96d08b5e5eb70d'
        country= self.kwargs.get('country')
        category= self.kwargs.get('category')
        url= f"https://newsapi.org/v2/top-headlines?category={category}&country={country}&apiKey={apikey}"
        response=requests.get(url)
        d=response.json()
        articles=d['articles']
        article = articles[index]
        context['article'] = article
        article_url = article['url']
        comments = models.comments.objects.filter(article_url=article_url)  
        context['comments'] = comments

        context['form'] = forms.CommentForm()  

        return context
    
    def post(self, request,**kwargs):
        context = self.get_context_data(**kwargs)
        comment_form= forms.CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            if request.user.is_authenticated:  # Check if the user is authenticated
               comment.user = request.user  # Assign the authenticated user to the comment's user field
               article_url = context['article'].get('url', '')  # Replace 'url' with the actual key in your article data
               comment.article_url = article_url
               comment.save()
            return self.get(request,**kwargs)
        else:
           return self.get(request,**kwargs)
        

class NewsSearchView(TemplateView):
    template_name = "search.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_query = self.request.GET.get('q')
        
        if search_query:
            api_key = 'your_api_key'
            url = f"https://newsapi.org/v2/everything?q={search_query}&apiKey={api_key}"
            response = requests.get(url)
            data = response.json()
            print(data)  # Print the API response for debugging

            articles = data.get('articles', [])
            context['search_query'] = search_query
            context['search_results'] = articles
        context['form']='None'
        return context


 
   
