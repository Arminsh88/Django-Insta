# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-02 11:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_profile', '0001_initial'),
        ('user_manager', '0001_initial'),
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='disc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discs', to='user_profile.Media'),
        ),
        migrations.AddField(
            model_name='upload',
            name='up_file',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploads', to='user_profile.Media'),
        ),
        migrations.AddField(
            model_name='upload',
            name='up_loc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_profile.Location'),
        ),
        migrations.AddField(
            model_name='upload',
            name='uploader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='report',
            name='which',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_profile.Media'),
        ),
        migrations.AddField(
            model_name='report',
            name='who',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reporter', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='report',
            name='whom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reported', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='like',
            name='what',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poster', to='user_profile.Media'),
        ),
        migrations.AddField(
            model_name='like',
            name='who',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liker', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='follow',
            name='who',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Following', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='follow',
            name='whom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Followers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='media_file',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_profile.Media'),
        ),
        migrations.AddField(
            model_name='comment',
            name='who',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='block',
            name='who',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blocker', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='block',
            name='whom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blocked', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='member',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='member',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
