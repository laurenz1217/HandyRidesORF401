# Generated by Django 5.1.6 on 2025-03-02 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='name',
            new_name='first_name',
        ),
    ]
