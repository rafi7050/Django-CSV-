# Generated by Django 3.2.5 on 2021-07-27 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last Name')),
                ('profile_picture', models.ImageField(upload_to=None, verbose_name='Profile Picture')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('phone_number', models.TextField(max_length=11, verbose_name='Phone Number')),
                ('room_number', models.TextField(max_length=25, verbose_name='Room Number')),
                ('Subject_1', models.TextField(max_length=100, verbose_name='Occupation')),
                ('Subject_2', models.TextField(max_length=100, verbose_name='Occupation')),
                ('Subject_3', models.TextField(max_length=100, verbose_name='Occupation')),
                ('Subject_4', models.TextField(max_length=100, verbose_name='Occupation')),
                ('Subject_5', models.TextField(max_length=100, verbose_name='Occupation')),
            ],
        ),
    ]
