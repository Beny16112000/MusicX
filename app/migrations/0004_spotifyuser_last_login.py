# Generated by Django 4.1.7 on 2023-02-16 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_cliendid_clientid'),
    ]

    operations = [
        migrations.AddField(
            model_name='spotifyuser',
            name='last_login',
            field=models.DateTimeField(auto_now=True),
        ),
    ]