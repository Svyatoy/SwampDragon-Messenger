from __future__ import unicode_literals

from PIL import Image
from django.core.urlresolvers import reverse
from django.db import models


class Company(models.Model):

    class Meta:
        verbose_name_plural = 'Companies'

    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    thumbnail = models.ImageField(upload_to='companies/thumbnails', max_length=500, null=True, blank=True)
    description = models.TextField(max_length=255, default='Just another company')
    ts_created = models.DateTimeField(auto_now_add=True)
    ts_updated = models.DateTimeField(auto_now=True)

    # def save(self, *args, **kwargs):
    #     if not self.id and not self.thumbnail:
    #         return
    #
    #     super(Company, self).save()
    #
    #     thumb = Image.open(self.thumbnail)
    #     width = thumb.width
    #     height = thumb.height
    #
    #     "Max width and height 200"
    #     if 200/width < 200/height:
    #         factor = 200.0/height
    #     else:
    #         factor = 200.0/width
    #
    #     size = (int(width / factor), int(height / factor))
    #     thumb.resize(size, Image.ANTIALIAS)
    #     thumb.save(self.thumbnail.path)
    #
    #     super(Company, self).save()

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('company-view', kwargs={'pk': self.id})
