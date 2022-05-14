from django.contrib import admin

from .models import Product, Tag, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'uuid', 'comma_price', 'category', 'is_active', 'is_take_away']
    search_fields = ['title', 'description', 'uuid']
    list_filter = ('category', 'is_active', 'is_take_away')

    def comma_price(self, instance: Product) -> str:
        return instance.comma_price(instance.price_as_toman)
    comma_price.short_description = 'price'


@admin.register(Tag, Category)
class TagCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    