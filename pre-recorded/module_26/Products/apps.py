from django.apps import AppConfig


class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Products'
    verbose_name = 'Products'

# you can add additional configuration options here if needed, such as custom signals or model registration.