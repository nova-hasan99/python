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
# the generated_code variable now contains the code from test/test.py up to the "# --- IGNORE ---" line. You can use this variable as needed in your script.
# from pathlib import Path
