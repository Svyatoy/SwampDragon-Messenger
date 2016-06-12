from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models


class News(models.Model):

    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000, default='Lorem ipsum dolor sit amet...')
    author = models.ForeignKey(User,
                               db_constraint=False,
                               related_name='news_written',
                               null=True)
    ts_created = models.DateTimeField(auto_now_add=True)
    ts_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'News'
        ordering = ['-ts_created']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news-view', kwargs={'pk': self.id})
