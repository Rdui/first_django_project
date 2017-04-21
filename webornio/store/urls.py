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
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^games/$', views.games, name='games'),
    url(r'^developer/$', views.devgames, name='developer'),
    url(r'^developer/game/(?P<game_id>[0-9]+)/$', views.devgame, name='devgame'),
    url(r'^developer/game/modify/(?P<game_id>[0-9]+)$', views.modifygame, name='modifygame')
    #url(r'^admin/', admin.site.urls),

]
