# Generated by Django 3.2.6 on 2022-06-10 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_book_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='n_votes',
            field=models.IntegerField(default=0),
        ),
    ]