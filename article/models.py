from django.db import models
from datetime import datetime
from django.utils.text import slugify


class Article_Info(models.Model):
    image = models.ImageField(upload_to='article_img')
    title = models.CharField(max_length=100)
    small_description = models.CharField(
        max_length=150, verbose_name='Description')
    owner = models.CharField(max_length=50)
    at_time = models.DateTimeField(default=datetime.now)
    type_section = models.ForeignKey('Section', on_delete=models.CASCADE)
    important_qouts = models.TextField(max_length=5000, null=True, blank=True)
    paragraph1 = models.TextField(max_length=50000)
    paragraph2 = models.TextField(max_length=50000)
    paragraph3 = models.TextField(max_length=50000, null=True, blank=True)
    paragraph4 = models.TextField(max_length=50000, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article_Info, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ' Add Article'
        ordering = ['title']


class Section(models.Model):
    section = models.CharField(max_length=50)

    def __str__(self):
        return self.section


class Comment(models.Model):
    post = models.ForeignKey(
        Article_Info, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
