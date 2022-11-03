from django.conf.urls import include
from django.urls import path
from django_project.views import HomeView
from django.contrib import admin

urlpatterns = [
    path('', HomeView.as_view()),
    path('admin/', admin.site.urls),
]
