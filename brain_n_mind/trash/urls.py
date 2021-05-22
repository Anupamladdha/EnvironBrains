# from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from .views import current_datetime

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('datetime/', current_datetime)
]