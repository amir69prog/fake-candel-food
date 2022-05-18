from django.contrib import admin

from .models import FavoriteProductList, Product, ProductComment, Tag, Category


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
    

@admin.register(ProductComment)
class ProductCommentAdmin(admin.ModelAdmin):
    list_display = ['product', 'name', 'email', 'website_url']
    search_fields = ('product', 'name', 'email', 'content', 'website_url')


@admin.register(FavoriteProductList)
class FavoriteProductListAdmin(admin.ModelAdmin):
    list_display = ['ip_address', 'count_list']
    search_fields = ('ip_address',)
