# Generated by Django 5.1.6 on 2025-03-31 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_usersignup_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersignup',
            name='photo',
            field=models.ImageField(upload_to='Photo'),
        ),
    ]
