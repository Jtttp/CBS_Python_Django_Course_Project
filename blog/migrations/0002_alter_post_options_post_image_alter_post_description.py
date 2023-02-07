# Generated by Django 4.1.6 on 2023-02-03 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Post'},
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='img.jpg', upload_to='image/%Y', verbose_name='Зображення'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(verbose_name='Текст допису'),
        ),
    ]
