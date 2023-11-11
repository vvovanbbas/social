# Generated by Django 4.1.7 on 2023-11-04 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=200, verbose_name='ФИО')),
                ('login', models.CharField(max_length=200, verbose_name='Login')),
                ('password', models.CharField(max_length=200, verbose_name='Password')),
                ('avatar', models.ImageField(upload_to='soc/social/avatars', verbose_name='Аватар')),
                ('date', models.DateField(verbose_name='Дата рождения')),
                ('city', models.CharField(max_length=200, verbose_name='Город')),
            ],
        ),
        migrations.CreateModel(
            name='Panel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=200, verbose_name='Заголовок')),
                ('description', models.CharField(default='', max_length=200, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='soc/social/panels', verbose_name='Картинка')),
                ('iduser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social.user')),
            ],
        ),
    ]
