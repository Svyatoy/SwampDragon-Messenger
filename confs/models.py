from __future__ import unicode_literals
from companies.models import Company
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
import datetime

from django.utils import timezone


class Conference(models.Model):
    title = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    description = models.TextField(max_length=255, default='Just another conference')
    event_date = models.DateTimeField(default=datetime.datetime.now() + datetime.timedelta(days=20))
    deadline = models.DateTimeField(default=datetime.datetime.now() + datetime.timedelta(days=10))
    listeners = models.ManyToManyField(User, related_name='conf_listener')
    reporters = models.ManyToManyField(User, related_name='conf_reporter')
    sponsors = models.ManyToManyField(Company, related_name='conf_sponsor')
    ts_created = models.DateTimeField(auto_now_add=True)
    ts_updated = models.DateTimeField(auto_now=True)

    def is_over(self):
        return self.event_date < timezone.now()

    def is_register_available(self):
        return self.deadline > timezone.now()

    def get_absolute_url(self):
        return reverse('conference-view', kwargs={'pk': self.id})

    def __unicode__(self):
        return self.title

    # def __str__(self):
    #     return ', '.join([
    #         '"' + str(self.title) + '"',
    #         self.event_date.strftime("%Y-%m-%d %H:%M:%S")
    #         ])
