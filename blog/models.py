from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse



class PublishedManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status=Post.Status.PUBLISHED)

class Post(models.Model):

    objects = models.Manager()
    published = PublishedManager()
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'


    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,unique_for_date='publish')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,choices=Status,default=Status.DRAFT)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='blog_post',null=True)

    class Meta:
        ordering = ['-publish']
        indexes = [models.Index(fields=['-publish'])]


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        # return reverse("blog:post_detail", args=[self.id,self.slug])
        return reverse("blog:post_detail", args=[self.publish.year,self.publish.month,self.publish.day,self.slug])
    