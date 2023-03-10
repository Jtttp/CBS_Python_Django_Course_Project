# Generated by Django 4.1.6 on 2023-02-04 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_options_post_image_alter_post_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=50, verbose_name="Ім'я користувача")),
                ('text_comments', models.TextField(max_length=2000, verbose_name='Текст для коментарів')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post', verbose_name='Публікація')),
            ],
            options={
                'verbose_name': 'Коментар',
            },
        ),
    ]
