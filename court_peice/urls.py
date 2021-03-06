from django.urls import path,include
from . import views

urlpatterns = [
    path('new-game',views.OpenTable),
    path('game/<slug:slug>',views.ShowTable),
    path('game/<slug:slug>/calculateRoundResult',views.CalculateRoundResult,name='CalRoundResult'),
    path('game/<slug:code>/<slug:name>',views.CustomTableForOne,name='showMyTableView'),
    path('game/<slug:code>/<slug:name>/addCard',views.AddCardToRound,name='AddCardToRound')
]
