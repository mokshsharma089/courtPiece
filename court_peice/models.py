from django.db import models

# Create your models here.

class Game(models.Model):
    SUIT_CHOICES = [
        ('DI','DIAMOND'),
        ('SP','SPADE'),
        ('HE','HEART'),
        ('CL','CLUB'),
    ]
    code=models.CharField(max_length=5,unique=True)
    trumpSuit=models.CharField(max_length=2,choices=SUIT_CHOICES,blank=False,default='SP')
    SP_wt=models.IntegerField(default=10000)
    DI_wt=models.IntegerField(default=200)
    HE_wt=models.IntegerField(default=300)
    CL_wt=models.IntegerField(default=400)
    def __str__(self):
        return '{0}'.format(self.code)

class Player(models.Model):
    game=models.ForeignKey(Game,on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    score=models.IntegerField(default=0)
    def __str__(self):
        return '{0}'.format(self.name)

class Round(models.Model):
    SUIT_CHOICES = [
        ('DI','DIAMOND'),
        ('SP','SPADE'),
        ('HE','HEART'),
        ('CL','CLUB'),
    ]
    RANK_CHOICES=[
        ('A','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9'),
        ('X','10'),
        ('J','11'),
        ('Q','12'),
        ('K','13'),
    ]
    game=models.ForeignKey(Game,on_delete=models.CASCADE)
    player=models.OneToOneField(Player,on_delete=models.CASCADE)
    suit=models.CharField(max_length=2,choices=SUIT_CHOICES)
    rank=models.CharField(max_length=1,choices=RANK_CHOICES)
    strongSuit=models.CharField(max_length=2,choices=SUIT_CHOICES)
    def __str__(self):
        return 'Game {0},Player {1},{2}-{3}'.format(self.game,self.player,self.suit,self.rank)

class Card(models.Model):
    SUIT_CHOICES = [
        ('DI','DIAMOND'),
        ('SP','SPADE'),
        ('HE','HEART'),
        ('CL','CLUB'),
    ]
    RANK_CHOICES=[
        ('A','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9'),
        ('X','10'),
        ('J','11'),
        ('Q','12'),
        ('K','13'),
    ]
    suit = models.CharField(max_length=2,choices=SUIT_CHOICES)
    rank=models.CharField(max_length=1,choices=RANK_CHOICES)
    player=models.ForeignKey(Player,on_delete=models.CASCADE)
    game=models.ForeignKey(Game,on_delete=models.CASCADE)

    def __str__(self):
        return '{2}, == {0}-{1}'.format(self.suit,self.rank,self.game)
