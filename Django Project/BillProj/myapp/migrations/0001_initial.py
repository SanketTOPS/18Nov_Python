# Generated by Django 5.1.6 on 2025-03-26 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mybill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('qty', models.IntegerField()),
                ('price', models.IntegerField()),
                ('total', models.BigIntegerField()),
            ],
        ),
    ]
