#-*- coding:UTF-8 -*-
from django.shortcuts import render
from django.template import loader
from django.contrib.auth.models import User
from .models import Game, SaveGame, Player, Sale, Developer

from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import redirect

from django.shortcuts import redirect



import logging




from hashlib import md5

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
        player = Player.objects.get(user=request.user.id)
        saleObj = Sale.objects.filter(player=player.id, game=game_id)
        if not saleObj.exists():
            return redirect("/store/games/buy/" + game_id)

        game_entry = Game.objects.get(id=game_id)
        url = game_entry.url
        template = loader.get_template('store/game.html')
        context = RequestContext(request, {'game_url': url, 'game_id': game_id})
        return HttpResponse(template.render(context))
    else:
        return redirect('login')

def games(request):
    if request.user.is_authenticated:
        games = Game.objects.all()
        template = loader.get_template("store/games.html")
        context = RequestContext(request, {'games': games})

        return HttpResponse(template.render(context))
    else:
        return redirect('login')

def devgames(request):
    developer = Developer.objects.get(user=request.user.id)
    games = Game.objects.filter(developer=developer)
    template = loader.get_template("store/developer.html")
    context = RequestContext(request, {'games': games, 'user': request.user})
    return HttpResponse(template.render(context))

def devgame(request, game_id):
    if request.user.is_authenticated():
        game = Game.objects.get(id = game_id)
        developer = Developer.objects.get(user=request.user.id)
        if game.developer == developer:
            template = loader.get_template("store/devgame.html")
            context = RequestContext(request, {'user': request.user, 'game': game})
            return HttpResponse(template.render(context))
        return HttpResponse('Ei oo sun peli')
#TODO: ehkä varmentaminen develle: pitäis olla nyt oikein. Tarkistettava
def modifygame(request):
    if request.method == "POST":
        data = request.POST
        if request.user.is_authenticated():
            developer = Developer.objects.get(user=request.user.id)
            gameObj = Game.objects.filter(id=data["gameid"])
            if gameObj[0].developer == developer:
                gameObj.update(name=data["gamename"], price=data["gameprice"], url=data["gameurl"])

    return redirect('developer')

def addgamepage(request):
    if request.user.is_authenticated():
        template = loader.get_template("store/addgamepage.html")
        context = RequestContext(request, {'user': request.user})
        return HttpResponse(template.render(context))

def addgame(request):
    if request.method == "POST":
        data = request.POST
        if request.user.is_authenticated():
            developer = Developer.objects.get(user=request.user.id)
            gameObj = Game(developer=developer, url=data["gameurl"], name=data["gamename"], price=data["gameprice"] )
            gameObj.save()
            return redirect('developer')

    return redirect('login')

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
    template = loader.get_template('registration/logout.html')
    context = RequestContext(request,{})
    return HttpResponse(template.render(context))

    #return HttpResponse("Hei maailma, katsot logout indeksiä.")

def profile(request):
    template = loader.get_template('store/profile.html')
    context = RequestContext(request, {'user': request.user})

    return HttpResponse(template.render(context))

def buy_game(request, game_id):
    game_entry = Game.objects.get(id=game_id)

    template = loader.get_template("store/buy_game.html")
    game = game_entry
    developer = game.developer
    secret_key = "f783295fc61ae6f4c9c06ac78a61e33f"
    pid = game_id   #TODO: vaihda yksilölliseen payment id:seen.
    sid = "webornio"
    amount = game.price
    # checksumstr is the string concatenated above
    checksumstr = "pid={}&sid={}&amount={}&token={}".format(pid, sid, amount, secret_key)

    #seller id: webornio
    m = md5(checksumstr.encode("ascii"))
    checksum = m.hexdigest()

    # checksum is the value that should be used in the payment request
    postdata = {
        "pid": pid,
        "sid": sid,
        "amount": amount,
        "success_url": "localhost:8000/store/success",
        "cancel_url": "localhost:8000/store/cancel",
        "error_url": "localhost:8000/store/error",
        "checksum": checksum
    }
    context = RequestContext(request, {'user': request.user, 'game': game_entry, 'buy_data': postdata})

    return HttpResponse(template.render(context))


def buy_success(request):
    pid = request.GET.get("pid")
    result = request.GET.get("result")
    #TODO: tarkista checksum
    if (result == "success"):
        game_entry = Game.objects.get(id=pid)
        player = Player.objects.get(user=request.user.id)
        purchase = Sale(game=game_entry, player=player, price=game_entry.price)
        purchase.save()
        return redirect("/store/games/" + str(game_entry.id))
    return HttpResponse("Ostaminen epäonnistui")

def buy_cancel(request):
    pass

def buy_error(request):
    pass
    
def register(request):
    if request.method == "POST":
        data = request.POST
        print("yee")
        player = User.objects.create_user(username=data["username"], password=data["psw"])
        player.save()
        return redirect("/store/login")

    else:
        template = loader.get_template('registration/registration_form.html')
        context = RequestContext(request,{})
        return HttpResponse(template.render(context))
