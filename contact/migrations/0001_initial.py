# Generated by Django 3.2.8 on 2021-10-22 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_country', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=12)),
                ('available_Time', models.CharField(choices=[('Any Time', 'Any Time'), ('12 am', '6 am'), ('6 am', '12 pm'), ('12 pm', '6 pm'), ('6 pm', '12 am')], max_length=10)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
    ]
