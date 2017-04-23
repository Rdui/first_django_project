from django.conf.urls import url

from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^games/(?P<game_id>[0-9]+)/$', views.game, name='game'),
    url(r'^api/games/save/$', views.save, name='save'),
    url(r'^api/games/load/(?P<gameId>[0-9]+)/$', views.load, name='load'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^games/$', views.games, name='games'),
    url(r'^games/buy/(?P<game_id>[0-9]+)/$', views.buy_game, name='buy_game'),
    url(r'^developer/$', views.devgames, name='developer'),
    url(r'^developer/game/(?P<game_id>[0-9]+)/$', views.devgame, name='devgame'),
    url(r'^developer/game/modify/(?P<game_id>[0-9]+)$', views.modifygame, name='modifygame'),
    url(r'^games/buy/success/$', views.buy_success, name='buy_success'),
    url(r'^games/buy/cancel/$', views.buy_cancel, name='buy_cancel'),
    url(r'^games/buy/error/$', views.buy_error, name='buy_error'),
    url(r'^developer/game/modify/$', views.modifygame, name='modifygame'),
    url(r'^register/$', views.register, name='register'),
    url(r'^games/(?P<game_id>[0-9]+)/highscores/$', views.highscores, name='highscores'),
    url(r'^api/games/load/(?P<gameId>[0-9]+)/$', views.load, name='load'),
    url(r'^api/games/score/$', views.savescore, name='savescore'),

]
