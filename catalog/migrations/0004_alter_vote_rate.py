# Generated by Django 3.2.6 on 2022-06-10 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_vote_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='rate',
            field=models.IntegerField(),
        ),
    ]