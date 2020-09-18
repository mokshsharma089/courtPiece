import random,string
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
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
    

def ShowTable(request,slug):
    g=get_object_or_404(Game,code=slug)
    players=Player.objects.filter(game=g)
    roundDetails=Round.objects.filter(game=g)
    roundState=[]
    strSuit='NA'
    if roundDetails:
        for ro in roundDetails:
            tempRoundObject={
                "player":'playerName',
                "suit":'SPADES',
                "rank": '15'
            }
            strSuit=ro.strongSuit
            tempRoundObject["player"]=ro.player
            tempRoundObject["suit"]=ro.suit
            tempRoundObject["rank"]=ro.rank
            roundState.append(tempRoundObject)
    Player_Hand_list=[]
    for player in players:
        
        tempPlayerObject={
        'name':'aa',
        'score':0,
        'hand':[]
        }
        tempPlayerObject["name"]=player.name
        tempPlayerObject["score"]=player.score
        currentPlayerCards=Card.objects.filter(player=player)
        for card in currentPlayerCards:
            tempPlayerObject["hand"].append(card)
        Player_Hand_list.append(tempPlayerObject)
    context={
        "game":g,
        "round":roundState,
        'strongSuit':strSuit,
        'PlayerList':Player_Hand_list
        
    }
    return render(request,'table.html',context)

def calculateValueOfCard(suit,rank,StrongPattern,Patterns):
    cardValue=Patterns[suit]
    if(suit==StrongPattern):
        cardValue*=10
    cardValue+=PointsSystem[rank]
    return cardValue

def CalculateRoundResult(request,slug):
    g=get_object_or_404(Game,code=slug)
    patterns={
        "DI":g.DI_wt,
        "HE":g.HE_wt,
        "SP":g.SP_wt,
        "CL":g.CL_wt
    }
    roundDetailsQuerySet=Round.objects.filter(game=g)
    roundDetails=list(roundDetailsQuerySet)
    if len(roundDetails)<4:
        return HttpResponseRedirect('/game/{0}'.format(slug))
    else:
        winner=roundDetails[0].player
        StrPattern=roundDetails[0].strongSuit
        BestSuit=roundDetails[0].suit
        BestRank=roundDetails[0].rank
        BestCardValue=calculateValueOfCard(BestSuit,BestRank,StrPattern,patterns)
        j=1
        for i in range(1,4):
            player=roundDetails[j].player
            SuitPlayed=roundDetails[j].suit
            RankPlayed=roundDetails[j].rank
            CardPlayedValue=calculateValueOfCard(SuitPlayed,RankPlayed,StrPattern,patterns)
            if  CardPlayedValue>BestCardValue:
                winner=player
                BestSuit=SuitPlayed
                BestRank=RankPlayed
                BestCardValue=CardPlayedValue
            j+=1
        playerWhoWon=Player.objects.get(game=g,name=winner.name)
        playerWhoWon.score+=1
        playerWhoWon.save()
        messages.info(request, "{0} won by playing {1}-{2} and his CardValue was {3}".format(winner,BestSuit,BestRank,BestCardValue))
        # print("{0} won by playing {1}-{2} and his score is {3}".format(winner,BestSuit,BestRank,BestCardValue))
        for obj in roundDetailsQuerySet:
            obj.delete()
        return HttpResponseRedirect('/game/{0}'.format(slug))
        
        
    # roundState=[]
    # if roundDetails:
    #     for ro in roundDetails:
    #         tempRoundObject={
    #             "player":'playerName',
    #             "suit":'SPADES',
    #             "rank": '15'
    #         }
    #         tempRoundObject["player"]=ro.player
    #         tempRoundObject["suit"]=ro.suit
    #         tempRoundObject["rank"]=ro.rank
    #         roundState.append(tempRoundObject)

