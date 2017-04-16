#-*- coding:UTF-8 -*-
from django.shortcuts import render
from django.template import loader
from .models import Game, SaveGame, Player

from django.http import HttpResponse
from django.template import RequestContext

from django.views.decorators.csrf import ensure_csrf_cookie
@ensure_csrf_cookie


def index(request):
    return HttpResponse("Hei maailma, katsot storen indeksiä.")

def game(request, game_id):
    game_entry = Game.objects.get(id=game_id)
    url = game_entry.url
    template = loader.get_template('store/game.html')
    context = RequestContext(request, {'game_url': url, 'game_id': game_id})

    return HttpResponse(template.render(context))

def save(request):
    if request.method == "POST":
        data = request.POST
        if request.user.is_authenticated():
            game = Game.objects.get(id=data["gameId"])
            userId = request.user.id
            user = Player.objects.get(id=userId)

            saveObj = SaveGame.objects.filter(player=user, game=game)
            if (saveObj.exists()):
                saveObj.gameState = data["gameState"]
                saveObj.update()
            else:
                saveObj = SaveGame(player=user, game=game, gameState=data["gameState"])
                saveObj.save()
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=403)
