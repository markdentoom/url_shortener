# Generated by Django 3.1.2 on 2024-03-06 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='short_url',
            field=models.TextField(blank=True),
        ),
    ]
