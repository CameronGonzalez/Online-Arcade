from django.conf.urls import url, include
from . import views

urlpatterns=[
   url(r'^$', views.index, name='index'),
   url(r'^snake/$', views.snake, name='snake'),
   url(r'^pong/$', views.pong, name='pong'),
   url(r'^spaceinvaders/$', views.spaceInvaders, name='spaceinvaders'),
   url(r'^tetris/$', views.tetris, name='tetris'),
   url(r'^pacman/$', views.pacMan, name='pacman'),
   url(r'^brickbreaker/$', views.brickBreaker, name='brickbreaker'),
   url(r'^avalanche/$', views.avalanche, name='avalanche'),
   url(r'^fishy/$', views.fishy, name='fishy'),
   url(r'^mimelet/$', views.mimelet, name='mimelet'),
   url(r'^pyro/$', views.pyro, name='pyro'),
   url(r'^agario/$', views.agario, name='agario'),
   url(r'^splixio/$', views.splixio, name='splixio'),  
]
