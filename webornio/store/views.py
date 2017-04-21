#-*- coding:UTF-8 -*-
from django.shortcuts import render
from django.template import loader
from .models import Game, SaveGame, Player, Sale

from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import redirect

import json

from django.views.decorators.csrf import ensure_csrf_cookie
@ensure_csrf_cookie


def index(request):
    template = loader.get_template('store/home.html')
    context = RequestContext(request, {'game_url': url, 'game_id': game_id})

    return HttpResponse(template.render(context))
    
def game(request, game_id):
    #Check if the user is authenticated and owns the game
    if request.user.is_authenticated():
        saleObj = Sale.objects.filter(id=request.user.id, game=game_id)
        if not saleObj.exists():
            return HttpResponse('et omista ko. peliä')

        game_entry = Game.objects.get(id=game_id)
        url = game_entry.url
        template = loader.get_template('store/game.html')
        context = RequestContext(request, {'game_url': url, 'game_id': game_id})

<<<<<<< HEAD
    return HttpResponse(template.render(context))
def games(request):
    games = Game.objects.all()
    template = loader.get_template("store/games.html")
    context = RequestContext(request, {'games': games})

    return HttpResponse(template.render(context))

=======
        return HttpResponse(template.render(context))
    else:
        return redirect('login')
>>>>>>> 479b20c922f9e5bc8799ef74f267b05111133c71

def save(request):
    if request.method == "POST":
        data = request.POST
        if request.user.is_authenticated():
            game = Game.objects.get(id=data["gameId"])
            userId = request.user.id
            user = Player.objects.get(id=userId)

            saveObj = SaveGame.objects.filter(player=user, game=game)
            if (saveObj.exists()):
                saveObj.update(gameState=data["gameState"])
            else:
                saveObj = SaveGame(player=user, game=game, gameState=data["gameState"])
                saveObj.save()
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=403)

def load(request, gameId):
    if request.user.is_authenticated():
        game = Game.objects.get(id=gameId)
        userId = request.user.id
        user = Player.objects.get(id=userId)

        saveObj = SaveGame.objects.filter(player=user, game=game)
        if (saveObj.exists()):
            print(saveObj[0].gameState)
            response = saveObj[0].gameState
            return HttpResponse(response)
        else:
            return HttpResponse(status=404)
    else:
        return HttpResponse(status=403)

def login(request):
    return HttpResponse("Hei maailma, katsot login.")
def logout(request):
    return HttpResponse("Hei maailma, katsot logout indeksiä.")

def profile(request):
    template = loader.get_template('store/profile.html')
    context = RequestContext(request, {'user': request.user})

    return HttpResponse(template.render(context))
