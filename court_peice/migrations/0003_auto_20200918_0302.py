# Generated by Django 3.1.1 on 2020-09-18 03:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('court_peice', '0002_auto_20200917_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='round',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='court_peice.game'),
        ),
    ]
