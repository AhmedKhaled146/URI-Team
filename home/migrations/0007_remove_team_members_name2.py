# Generated by Django 3.2.8 on 2021-10-24 03:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_team_members_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team_members',
            name='name2',
        ),
    ]
