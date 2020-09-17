import random
deck=[
    'DI-A','DI-2','DI-3','DI-4','DI-5','DI-6','DI-7','DI-8','DI-9','DI-X','DI-J','DI-Q','DI-K',
    'HE-A','HE-2','HE-3','HE-4','HE-5','HE-6','HE-7','HE-8','HE-9','HE-X','HE-J','HE-Q','HE-K',
    'SP-A','SP-2','SP-3','SP-4','SP-5','SP-6','SP-7','SP-8','SP-9','SP-X','SP-J','SP-Q','SP-K',
    'CL-A','CL-2','CL-3','CL-4','CL-5','CL-6','CL-7','CL-8','CL-9','CL-X','CL-J','CL-Q','CL-K'
]
PointsSystem={
    'A':14,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'X':10,'J':11,'Q':12,'K':13
}
patterns={
    "DI":100,
    "HE":200,
    "SP":1000000,
    "CL":400
}
playerA={
    "name":"A",
    "hand":[],
    "score":0
    }
playerB={
    "name":"B",
    "hand":[],
    "score":0
}
playerC={
    "name":"C",
    "hand":[],
    "score":0
}
playerD={
    "name":"D",
    "hand":[],
    "score":0
}
Players=[playerA,playerB,playerC,playerD]
trump="SP"

def printDeck():
    print('At this moment the deck contains {0} cards'.format(len(deck)))
    for i in range(len(deck)):
        print(deck[i],end=" ")
    print()

def PrintPlayerHand(Player):
    print('player {0}, has {1} cards and the current hand is :- '.format(Player["name"],len(Player["hand"])))
    for i in Player["hand"]:
        print(i,end=" ")
    print()

def DivideCardsAmongstPlayers(len,PlayersList):
    for player in PlayersList:
        for i in range(len):
            a=random.choice(deck)
            deck.remove(a)
            player["hand"].append(a)

def PrintAllPlayerHands(PlayersList):
    for player in PlayersList:
        PrintPlayerHand(player)
    print()

def SortHandsAccToType(PlayersList):
    for player in PlayersList:
        player["hand"].sort()
    print()

def calculateValueOfCard(card,StrongPattern):
    cardPattern=card[0:2]
    cardValue=patterns[cardPattern]
    if(cardPattern==StrongPattern):
        cardValue*=10
    cardValue+=PointsSystem[card[3]]
    return cardValue

def CalcuteHandResult(playerAndCardPlayedTuple):
    winner=playerAndCardPlayedTuple[0][0]
    BestCard=playerAndCardPlayedTuple[0][1]
    StrongPattern=BestCard[0:2]
    BestCardValue=calculateValueOfCard(BestCard,StrongPattern)
    for i in range(1,4):
        player=playerAndCardPlayedTuple[i][0]
        CardPlayed=playerAndCardPlayedTuple[i][1]
        CardPlayedValue=calculateValueOfCard(CardPlayed,StrongPattern)
        if  CardPlayedValue>BestCardValue:
            winner=player
            BestCard=CardPlayed
            BestCardValue=CardPlayedValue
    winner["score"]+=1
    print("{0} won by playing {1} and his score is {2}".format(winner["name"],BestCard,winner["score"]))


            
# printDeck()
# print("1st distribution of cards")
# DivideCardsAmongstPlayers(5,Players)
# printDeck()
# print()
# PrintAllPlayerHands(Players)
# print()
# print("2nd distribution of cards")
# DivideCardsAmongstPlayers(8,Players)
# printDeck()
# print()
# PrintAllPlayerHands(Players)
# print()
# print("after Sorting Acc to Type")
# SortHandsAccToType(Players)
# print()
# PrintAllPlayerHands(Players)
# print()

# hand=[
#     'SP-6','SP-7','SP-8','SP-9','SP-X','SP-J','SP-Q','CL-A','HE-9','HE-X','HE-J','HE-Q','HE-K','DI-3','DI-4'
# ]
# print("the trump is spades and strong hand is of clubs ==")
# for i in hand:
#     print("For Card {0} the calculated Value is :- {1}".format(i,calculateValueOfCard(i,'CL')))

AllPlayerHand=[
    (playerA,'CL-6'),
    (playerB,'CL-4'),
    (playerC,'CL-9'),
    (playerD,'SP-2')
]
CalcuteHandResult(AllPlayerHand)
AllPlayerHand=[
    (playerA,'HE-6'),
    (playerB,'CL-4'),
    (playerC,'CL-9'),
    (playerD,'SP-3')
]
CalcuteHandResult(AllPlayerHand)