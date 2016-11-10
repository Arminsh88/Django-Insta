from django.contrib.auth.models import AbstractUser
from django.db import models
from model_utils.models import TimeStampedModel
# Create your models here.
from user_profile.models import Media, Location


class Member(AbstractUser):
    phone = models.CharField(max_length=15, validators=[]) #TODO: Add validator
    bio = models.TextField(max_length=500)
    profile_picture = models.ImageField(upload_to="")


class Follow(TimeStampedModel):
    who = models.ForeignKey(Member, null=False, related_name="Following")
    whom = models.ForeignKey(Member, null=False, related_name="Followers")

    def save(self, *args, **kwargs):
        if self.who != self.whom:
            super(Follow, self).save(*args, **kwargs)
        else:
            raise ValueError("You cannot follow yourself")


    class Meta:
        unique_together = ('who', 'whom')



class Block(TimeStampedModel):
    who = models.ForeignKey(Member, null=False, related_name="blocker")
    whom = models.ForeignKey(Member, null=False,related_name= "blocked")
    class Meta:
        unique_together = ('who', 'whom')

class Upload(TimeStampedModel):
    uploader = models.ForeignKey(Member, null=False)
    up_file = models.ForeignKey(Media, null=False, related_name="uploads")
    disc = models.ForeignKey(Media,related_name='discs')
    up_loc = models.ForeignKey(Location)



class Like(TimeStampedModel):
    who = models.ForeignKey(Member, null=False, related_name="liker")
    what = models.ForeignKey(Media, null=False, related_name="poster")

    def __str__(self):
        return '{name} liked {obj}'.format(name=self.who.get_full_name(),
                                           obj=self.what.media_disc)


class Comment(TimeStampedModel):
    who = models.ForeignKey(Member, null=False)
    media_file = models.ForeignKey(Media, null=False)
    comment_text = models.TextField()

    def __str__(self):
        return '{name} commented {cm}.'.format(name=self.who.get_full_name(),
                                               cm=self.comment_text)


class Report(TimeStampedModel):
    who = models.ForeignKey(Member, null=False, related_name='reporter')
    whom = models.ForeignKey(Member, null=False, related_name='reported')
    which = models.ForeignKey(Media)

    class Meta:
        unique_together = ('who', 'whom')
