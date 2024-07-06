import os
import sys
from dotenv import load_dotenv
from django.core.management.commands.runserver import Command as runserver
load_dotenv()

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    runserver.default_port = os.getenv('SERVICE_PORT')
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()