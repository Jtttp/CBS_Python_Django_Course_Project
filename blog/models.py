from django.db import models


class Post(models.Model):
    """This class creates posts in blog"""
    title = models.CharField('Заголовок', max_length=100)
    description = models.TextField('Текст допису')
    author = models.CharField('Автор', max_length=50)
    date = models.DateField('Дата публікації')
    image = models.ImageField('Зображення', upload_to='image/%Y')

    def __str__(self):
        return f'{self.title}, {self.author}'

    class Meta:
        verbose_name = 'Post'


class Comments(models.Model):
    """Page guests could write their comments"""
    email = models.EmailField()
    name = models.CharField('Ім\'я користувача', max_length=50)
    text_comments = models.TextField('Текст для коментарів', max_length=2000)
    post = models.ForeignKey(Post, verbose_name='Публікація', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.post}'

    class Meta:
        verbose_name = 'Comment'


class Likes(models.Model):
    """Page guests could add likes"""
    ip = models.CharField('IP-адреса', max_length=100)
    pos = models.ForeignKey(Post, verbose_name='Публікація', on_delete=models.CASCADE)
