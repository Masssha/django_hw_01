from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

class Tag(models.Model):
    name = models.CharField(max_length=256, verbose_name='Категория')
    # articles = models.ManyToManyField(Article, related_name='tag')

class Scope(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='scopes')
    is_main = models.BooleanField(default=False)
    title = models.CharField(max_length=256, verbose_name='Scope_title', default='почему-то это поле требовал джанго :D')

    def __str__(self):
        return self.title
