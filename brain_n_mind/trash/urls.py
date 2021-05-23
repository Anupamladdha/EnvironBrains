# from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from .views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('datetime/', current_datetime),
    path('user/profile/', getUserProfile),
    path('user/data', getUserData)
]