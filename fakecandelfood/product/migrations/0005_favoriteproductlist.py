# Generated by Django 4.0.4 on 2022-05-17 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_productcomment_website_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteProductList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField(unique=True, verbose_name='IP')),
                ('products', models.ManyToManyField(blank=True, related_name='favorites', to='product.product')),
            ],
        ),
    ]
