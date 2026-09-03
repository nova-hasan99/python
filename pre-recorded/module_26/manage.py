#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FastKart.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
   
   
# with open("test/test.py", "r") as file:
#     content = file.read()
# generated_code = content.split("# --- IGNORE ---")[0] 
# with open("test/test.py", "w") as file:
#     file.write(generated_code)
# my suggestion: The code in the `ProductsConfig` class looks good. If you want to add more functionality or configurations, you can do so by overriding methods like `ready()` or adding additional attributes. For example, if you want to perform some initialization when the app is ready, you can override the `ready()` method:
