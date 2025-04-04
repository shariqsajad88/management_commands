To export all the settings variables from your Django project and compare them across different environments,we need  follow these steps:

1. Export Settings Variables to a File
we can create a Django management command to list all settings variables and save them to a file.
Create a Custom Management Command
Inside your Django app (e.g., core), create a management/commands directory:

mkdir -p core/management/commands
Add an empty __init__.py file in each directory to make them Python packages:


touch core/management/__init__.py
touch core/management/commands/__init__.py

Create a new management command export_settings.py:

touch core/management/commands/export_settings.py


Run the command for different environments:

DJANGO_ENV=dev python manage.py export_settings
DJANGO_ENV=staging python manage.py export_settings
DJANGO_ENV=production python manage.py export_settings


To compare the generated JSON files, use diff, meld, or Python:
Using diff 
diff -u settings_dev.json settings_production.json
