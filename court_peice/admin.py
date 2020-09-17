from django.contrib import admin
from .models import Player,Card,Game,Round

# Register your models here.
admin.site.register([
    Game,
    Player,
    Card,
    Round
])