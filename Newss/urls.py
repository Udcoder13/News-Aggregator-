from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/',admin.site.urls),
    path('',views.index.as_view(),name='index'),
    path('news/',views.NewsList.as_view(),name='newslist'),
    path('news/detail/<int:pk>',views.NewsDetail.as_view(),name='newsdetail'),
    path('news/<str:country>/<str:category>/',views.CategoryView.as_view(),name='news-category-list'),
    path('news/detail/<str:country>/<str:category>/<int:index>/',views.CategoryDetailView.as_view(),name='news-detail'),
    path('news/search/', views.NewsSearchView.as_view(), name='news-search'),

  ]
