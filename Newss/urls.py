from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',views.index.as_view()),
    path('news/',views.NewsList.as_view(),name='newslist'),
    path('news/detail/<int:pk>',views.NewsDetail.as_view(),name='newsdetail')
]
