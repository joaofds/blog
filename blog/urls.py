from django.urls import path
from django.http import HttpResponse as Response
from .views import *

app_name = "blog"

urlpatterns = [
    path('', lambda request: Response("index"), name = 'index'),

    # post routes
    path('post', post.PostListView.as_view(), name = 'post_list')
]
