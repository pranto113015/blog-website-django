from django.urls import path
from . views import *

urlpatterns = [
    path('', home,name='index'),
    path('about/', about,name='about'),
    path('contact/', contact,name='contact'),
    path('article/blogdetails/<int:pk>/', blogdetails,name='blogdetails'),
]