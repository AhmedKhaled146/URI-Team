# Generated by Django 3.2.8 on 2021-10-16 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Who_We_are_URI', models.TextField(max_length=50000)),
                ('What_Do_We_Care_about_Why_Did_URI_Stablish', models.TextField(max_length=50000)),
                ('The_Goal_Of_Scientific_Research', models.TextField(max_length=50000)),
                ('What_Will_You_Benefit_From_URI', models.TextField(max_length=50000)),
                ('Beginning_Of_The_Story', models.TextField(max_length=50000)),
            ],
        ),
    ]
