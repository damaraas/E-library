# Generated by Django 5.1.6 on 2025-02-16 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_buku_delete_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='buku',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]
