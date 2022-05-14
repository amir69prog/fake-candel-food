from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampedModel(models.Model):
    """ an abstract model to provide timestamped fields """
    
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)
    
    class Meta:
        abstract = True



class SlugableModel(models.Model):
    """ an abstract model to provide slug field """

    slug = models.SlugField(_('Slug'), allow_unicode=True)
    
    class Meta:
        abstract = True