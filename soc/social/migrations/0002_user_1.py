# Generated by Django 4.2.7 on 2023-11-25 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=200, verbose_name='Login')),
                ('password', models.CharField(max_length=200, verbose_name='Password')),
            ],
        ),
    ]
