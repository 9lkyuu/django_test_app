from django.db import models
from djrichtextfield.models import RichTextField


class DateTimeStamp(models.Model):
    created = models.DateTimeField('created', auto_now=True)
    updated = models.DateTimeField('Updated', auto_now_add=True)

    class Meta:
        abstract = True


class Category(models.Model):
    name = models.CharField('Category name', max_length=25, unique=True)
    url = models.URLField('URL', blank=True)
    email = models.EmailField('Email', blank=True)
    description = models.TextField(verbose_name='Description', blank=True)
    activate = models.BooleanField('Active', default=False)
    created = models.DateTimeField('Created', auto_now_add=True)
    updated = models.DateTimeField('Updated', auto_now=True)

    class Meta:
        verbose_name = 'categories'
        verbose_name_plural = 'categories'
        ordering = ['name']

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField('Имя тега', max_length=25, unique=True)
    uuid = models.UUIDField('UUID')

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"
        ordering = ['-name']

    def __str__(self):
        return self.name



class Goods(DateTimeStamp):
    name = models.CharField('Goods name', max_length=25, unique=True)
    url = models.URLField('URL', blank=True)
    email = models.EmailField('Email', blank=True)
    description = models.TextField(verbose_name='Description', blank=True)
    activate = models.BooleanField('Active', default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='goods')
    tags = models.ManyToManyField(Tag, related_name='goods_tag')
    image = models.ImageField('Image', upload_to='image', blank=True)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'goods'
        ordering = ['name']

    def __str__(self):
        return self.name



