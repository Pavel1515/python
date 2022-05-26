# Generated by Django 4.0.4 on 2022-05-25 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-creat_up'], 'verbose_name': 'Новости', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AlterField(
            model_name='news',
            name='content',
            field=models.TextField(blank=True, verbose_name='Контент'),
        ),
        migrations.AlterField(
            model_name='news',
            name='creat_up',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления'),
        ),
        migrations.AlterField(
            model_name='news',
            name='is_publishen',
            field=models.BooleanField(default=True, verbose_name='Опубликовано?'),
        ),
        migrations.AlterField(
            model_name='news',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Наименования'),
        ),
        migrations.AlterField(
            model_name='news',
            name='update_up',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата обновления'),
        ),
    ]
