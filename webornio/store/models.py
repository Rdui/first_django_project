from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Player(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  def __str__(self):
    return (self.user.username.encode('utf-8'))


class Developer(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  def __str__(self):
    return (self.user.username.encode('utf-8'))

class Game(models.Model):
  name = models.CharField(max_length=100)
  price = models.IntegerField()
  developer = models.ForeignKey(Developer)
  url = models.CharField(max_length=333, default='')
  
  def __str__(self):
    return (self.name.encode('utf-8'))

class Sale(models.Model):
  game = models.ForeignKey(Game)
  player = models.ForeignKey(Player)
  price = models.IntegerField()

class SaveGame(models.Model):
  gameState = models.TextField()
  player = models.ForeignKey(Player)
  game = models.ForeignKey(Game)

class Score(models.Model):
  score = models.IntegerField()
  player = models.ForeignKey(Player)
  game = models.ForeignKey(Game)