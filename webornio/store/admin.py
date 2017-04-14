from django.contrib import admin

from .models import Game
from .models import Player
from .models import Developer
from .models import SaveGame
from .models import Sale
from .models import Score
# Register your models here.
admin.site.register(Game)
admin.site.register(Player)
admin.site.register(Developer)
admin.site.register(SaveGame)
admin.site.register(Sale)
admin.site.register(Score)
