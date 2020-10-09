from django.urls import path
from . import views
from django.conf import settings
from django.views.static import serve

app_name = "MySite"
urlpatterns = [
    path('', views.home, name="home"),
    path('essay/', views.essayIndex, name="essayIndex"),
    path('essay/<str:title>/', views.essay, name="essay"),
]
