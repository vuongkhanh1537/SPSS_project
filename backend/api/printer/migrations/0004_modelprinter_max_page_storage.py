# Generated by Django 4.2.6 on 2023-12-06 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_printer', '0003_modelprinter_page_per_min'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelprinter',
            name='max_page_storage',
            field=models.PositiveIntegerField(default=250),
        ),
    ]