"""ninja_gold URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from game import views

urlpatterns = [
    path('', views.index, name='index'),
    path('play', views.play, name='play'),
    path('process_money', views.process_money, name='process_money'),
    path('play_again', views.play_again, name='play_again'),
    path('view_scoreboard', views.view_scoreboard, name='view_scoreboard'),
    path('clear', views.play_again, name='clear'),
]