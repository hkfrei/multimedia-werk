# Generated by Django 4.1 on 2022-09-15 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kartenwerk', '0018_alter_angebot_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firma', models.CharField(max_length=100, verbose_name='Titel')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('vorname', models.CharField(max_length=50, verbose_name='Vorname')),
                ('position', models.CharField(max_length=100, verbose_name='Position')),
                ('text', models.TextField(verbose_name='Testimonial Text')),
                ('angebot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kartenwerk.angebot')),
            ],
            options={
                'verbose_name_plural': 'Testimonials',
            },
        ),
    ]