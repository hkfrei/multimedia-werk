# Generated by Django 4.1 on 2022-09-15 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kartenwerk', '0009_angebot_angebot_cards_beschrieb_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='angebot',
            name='subtitel',
            field=models.CharField(default='Subtitel', max_length=100, verbose_name='Subtitel'),
        ),
    ]