from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LoginView,LogoutView
from.import views
from .views import Logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.Register,name='register'),
    path('login/',LoginView.as_view(template_name="account/login.html"), name='login'),
    path('logout/',views.Logout, name='logout'),

  ]
