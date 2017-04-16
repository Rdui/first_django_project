from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^games/(?P<game_id>[0-9]+)/$', views.game, name='game'),
    url(r'^api/games/save/$', views.save, name='save'),
    url(r'^api/games/load/(?P<gameId>[0-9]+)/$', views.load, name='load'),

]
