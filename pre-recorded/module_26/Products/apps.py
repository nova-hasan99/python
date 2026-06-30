from django.apps import AppConfig


class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Products'

# This code defines a Django application configuration class named `ProductsConfig`. It inherits from `AppConfig`, which is the base class for all application configurations in Django. The `default_auto_field` attribute specifies the type of primary key field to use for models in this app, which is set to `BigAutoField`. The `name` attribute specifies the name of the application, which is 'Products'. This configuration class is used by Django to manage the app's settings and behavior.