import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'say_something.settings')
django.setup()

from django.contrib.auth.models import User

if not User.objects.filter(username='admin').exists():
    print("Creating default admin user...")
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print("Superuser 'admin' created with password 'admin123'")
else:
    print("Admin user already exists.")
