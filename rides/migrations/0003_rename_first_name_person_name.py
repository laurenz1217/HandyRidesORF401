# Generated by Django 5.1.6 on 2025-03-02 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0002_rename_name_person_first_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='first_name',
            new_name='name',
        ),
    ]
