# Generated by Django 4.1 on 2022-09-16 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kartenwerk', '0022_alter_stakeholder_firma'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referenz',
            name='bild',
            field=models.CharField(blank=True, max_length=50, verbose_name='Bild'),
        ),
        migrations.AlterField(
            model_name='referenz',
            name='video',
            field=models.CharField(blank=True, max_length=50, verbose_name='Video'),
        ),
    ]