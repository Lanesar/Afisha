# Generated by Django 4.0.5 on 2022-08-11 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0006_alter_movie_director_alter_movie_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='director',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
