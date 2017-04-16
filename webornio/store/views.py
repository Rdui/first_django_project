#-*- coding:UTF-8 -*-
from django.shortcuts import render
from django.template import loader


from django.http import HttpResponse


def index(request):
    return HttpResponse("Hei maailma, katsot storen indeksiä.")

def game(request, game_id):
    url = "HOMO"    #get URL from database
    template = loader.get_template('store/game.html')
    context = {
        'game_url': url,
    }
    return HttpResponse(template.render(context, request))
