from django.apps import AppConfig


class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Products'
    verbose_name = 'Products'


# https://docs.djangoproject.com/en/4.2/ref/applications/#django.apps.AppConfig.verbose_name