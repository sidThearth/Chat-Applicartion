import os
import django
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_project.settings')
django.setup()

from daphne.cli import CommandLineInterface

if __name__ == "__main__":
    cli = CommandLineInterface()
    port = os.getenv("PORT", "8001")  # Default to 8001 if PORT is not set
    cli.run(["-b", "0.0.0.0", "-p", port, "chat_project.asgi:application"])
