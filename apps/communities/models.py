from django import template
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

import misaka

User = get_user_model()
register = template.Library()


class Community(models.Model):
    name = models.CharField(max_length=256, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False, default='', blank=True)
    members = models.ManyToManyField(User, through='CommunityMember', related_name='communities')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('communities:single_community', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['name']


class CommunityMember(models.Model):
    community = models.ForeignKey(Community, related_name='communities', on_delete=models.PROTECT)
    user = models.ForeignKey(User, related_name='user_communities', on_delete=models.PROTECT)

    def __str__(self):
        return self.user.username

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['community', 'user'], name='unique_community_user')
        ]
