#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from backend.settings import base

def main():
    """Run administrative tasks."""
    # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
    # here we try to find something to distinguish between prod and local like DEBUG if we make it true will be local if false will be production

    if base.DEBUG:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings.development')
    else:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings.production')

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
