# Generated by Django 5.0.4 on 2024-12-04 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermodel',
            old_name='email',
            new_name='username',
        ),
    ]
