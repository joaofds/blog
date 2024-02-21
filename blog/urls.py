from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    # GET /
    path('', views.index, name = 'index')
]
