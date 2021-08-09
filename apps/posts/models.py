from django.contrib.auth import get_user_model
from django.db import models

import misaka
from django.urls import reverse

from apps.communities.models import Community

User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(User, related_name='post', on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    community = models.ForeignKey(Community, related_name='posts', null=True, blank=True, on_delete=models.RESTRICT)

    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('posts:single', kwargs={'username': self.user.username, 'pk': self.pk})

    class Meta:
        ordering = ['-created_at']
        constraints = [
            models.UniqueConstraint(fields=['user', 'message'], name='user_message_unique')
        ]
