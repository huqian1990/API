from . import views
from django.urls import path,re_path,include
urlpatterns = [
    path('login/',views.login,name='login'),
]
