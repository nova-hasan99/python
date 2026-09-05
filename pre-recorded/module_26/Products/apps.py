from django.apps import AppConfig


class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Products'
    verbose_name = 'Products'


# additional context: This is a recently edited file. Do not suggest code that has been deleted.
 # print(f"Minimum voltage: {summary['minimum_voltage']} V")
# print(f"Maximum voltage: {summary['maximum_voltage']} V")
# print(f"Voltage gain: {summary['voltage_gain']} V")
# print(f"Average slope: {summary['average_slope']:.2f} V/A")
# my suggestion: The code in the `ProductsConfig` class looks good. If you want to add more functionality or configurations, you can do so by overriding methods like `ready()` or adding additional attributes. For example, if you want to perform some initialization when the app is ready, you can override the `ready()` method:


