from django.contrib.auth.models import AbstractUser
from django.db import models
from model_utils.models import TimeStampedModel
# from user_manager.models import Member


class HashTag(models.Model):
    tag_id = models.CharField(max_length=50)

    def __str__(self):
        return self.tag_id


class Category(models.Model):
    cat_id = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'Categories'


class Location(models.Model):
    loc = models.TextField()


class Media(TimeStampedModel):
    user_id = models.ForeignKey('user_manager.Member', null=False, related_name="posts", verbose_name='User')
    media_id = models.FileField(null=False,verbose_name='Media File')
    media_disc = models.TextField(verbose_name='Description')
    media_cat = models.ForeignKey(Category, blank=True, null=True, verbose_name='Category')
    Media_loc = models.ForeignKey(Location, blank=True, null=True, verbose_name="Location")
    hash_tags = models.ManyToManyField(HashTag, blank=True, null=True, verbose_name='Hashtag')
    comments = models.ManyToManyField('user_manager.Member', through='user_manager.Comment')

    def __str__(self):
        return self.media_disc

    class Meta:
        verbose_name_plural = 'Media'


class Interests(models.Model):
    user = models.ForeignKey('user_manager.Member')
    cat = models.ForeignKey(Category)
    class Meta:
        verbose_name_plural = 'Interests'


class View(models.Model):
    who = models.ForeignKey('user_manager.Member')
    req_file = models.ForeignKey(Media)