import random,string
from django.shortcuts import render
from .models import Player,Card,Game,Round


PointsSystem={
    'A':14,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'X':10,'J':11,'Q':12,'K':13
}

def newRandomCode(size):
    return ''.join(random.choice(string.ascii_lowercase+ string.ascii_uppercase + string.digits) for _ in range(size) )

# def DivideCardsAmongstPlayers(len,PlayersList,deck,g):
#     for player in PlayersList:
#         for i in range(len):
#             a=random.choice(deck)
#             deck.remove(a)
#             s=a[0:2]
#             Card.objects.create(suit=s,rank=a[3],player=player,game=g)
            

def OpenTable(request):
    c=newRandomCode(4)
    g=Game.objects.create(code=c)
    names=['A','B','C','D']
    deck=[
    'DI-A','DI-2','DI-3','DI-4','DI-5','DI-6','DI-7','DI-8','DI-9','DI-X','DI-J','DI-Q','DI-K',
    'HE-A','HE-2','HE-3','HE-4','HE-5','HE-6','HE-7','HE-8','HE-9','HE-X','HE-J','HE-Q','HE-K',
    'SP-A','SP-2','SP-3','SP-4','SP-5','SP-6','SP-7','SP-8','SP-9','SP-X','SP-J','SP-Q','SP-K',
    'CL-A','CL-2','CL-3','CL-4','CL-5','CL-6','CL-7','CL-8','CL-9','CL-X','CL-J','CL-Q','CL-K'
    ]   
    playerList=[]
    A_hand=[]
    B_hand=[]
    C_hand=[]
    D_hand=[]
    Hand_list=[ A_hand,B_hand,C_hand,D_hand]
    for i in range(0,4):
        playerList.append(Player.objects.create(name=names[i],game=g))
    # DivideCardsAmongstPlayers(13,playerList,deck,g)
    j=0
    for player in playerList:
        for i in range(13):
            a=random.choice(deck)
            deck.remove(a)
            s=a[0:2]
            c=Card.objects.create(suit=s,rank=a[3],player=player,game=g)
            Hand_list[j].append(c)
        j+=1

    context={
        "game":g,
        "player_list":playerList,
        "A_hand":A_hand,
        "B_hand":B_hand,
        "C_hand":C_hand,
        "D_hand":D_hand,
    }
    return render(request,'table.html',context)
    


