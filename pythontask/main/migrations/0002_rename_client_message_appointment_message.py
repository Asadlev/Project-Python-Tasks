# Generated by Django 5.0.1 on 2024-02-05 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='client_message',
            new_name='message',
        ),
    ]
