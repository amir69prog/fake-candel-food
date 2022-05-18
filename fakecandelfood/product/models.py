from typing import Union
import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.humanize.templatetags.humanize import intcomma


from config.models import SlugableModel, TimeStampedModel


def get_product_cover_path(instance: 'Product', filename: str) -> str:
    """ Return specific path for storing product cover """
    return f'product_covers/{instance.title}/{filename}'


class Product(SlugableModel, TimeStampedModel, models.Model):
    uuid = models.UUIDField(
        _('UUID'),
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(_('Title'), max_length=256)
    price = models.DecimalField(_('Price'), max_digits=10, decimal_places=2)
    cover = models.ImageField(_('Cover'), upload_to=get_product_cover_path)
    category = models.ForeignKey(
        to='Category',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_('Category'),
        related_name='products'
    )
    tags = models.ManyToManyField(
        to='Tag',
        related_name='products',
        verbose_name=_('Tag')
    )
    description = models.TextField(_('Description'))
    is_active = models.BooleanField(_('Active'), default=True)
    is_take_away = models.BooleanField(_('Take away'), default=True)

    def __str__(self) -> str:
        return self.slug

    @property
    def price_as_toman(self):
        """ Price as toman """
        return int(self.price)
    
    def comma_price(self, price: Union[int, float]) -> str:
        """ Comma the price """
        return intcomma(price)


class Category(SlugableModel, models.Model):
    title = models.CharField(_('Title'), max_length=128)

    class Meta:
        verbose_name_plural = _('Categories')

    def __str__(self) -> str:
        return self.title


class Tag(SlugableModel, models.Model):
    title = models.CharField(_('Title'), max_length=128)

    def __str__(self) -> str:
        return self.title
    

class ProductComment(models.Model):
    content = models.TextField(_('Content'))
    name = models.CharField(_('Name'), max_length=128)
    email = models.EmailField(_('Email'), max_length=256)
    website_url = models.URLField(_('Website URL'), blank=True, null=True)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='product_comments',
        verbose_name=_('Product')
    )

    def __str__(self) -> str:
        return self.name


class FavoriteProductList(models.Model):
    ip_address = models.GenericIPAddressField(_('IP'), unique=True,)
    products = models.ManyToManyField(Product, related_name='favorites', blank=True)

    def __str__(self) -> str:
        return self.ip_address
    
    @property
    def count_list(self) -> int:
        """ Return count of the products list """
        return self.products.count()