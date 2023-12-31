# Generated by Django 4.2.6 on 2023-12-02 10:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inst', models.IntegerField(choices=[(1, 'Cơ sở 1'), (2, 'Cơ sở 2')], default=1)),
                ('building', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('floor_code', models.PositiveIntegerField()),
                ('building_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_printer.building')),
            ],
        ),
        migrations.CreateModel(
            name='ModelPrinter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=12)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='model_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='model_modified_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Printer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('pages_remaining', models.PositiveIntegerField()),
                ('ink_status', models.BooleanField(default=True)),
                ('status', models.IntegerField(choices=[(1, 'Active'), (3, 'Offline'), (4, 'Error'), (5, 'Busy'), (2, 'Maintenance')], default=1)),
                ('floor_description', models.CharField(blank=True, max_length=255, null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='created_by', to=settings.AUTH_USER_MODEL)),
                ('floor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='printer_floor', to='api_printer.floor')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_printer.modelprinter')),
                ('modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='modified_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_at',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderPrinter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_upload', models.FileField(upload_to='local/')),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('is_printed', models.BooleanField(default=False)),
                ('print_date', models.DateTimeField(blank=True, null=True)),
                ('is_cancelled', models.BooleanField(default=False)),
                ('file_name', models.CharField(max_length=50)),
                ('pages', models.PositiveIntegerField()),
                ('printer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api_printer.printer')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature', models.CharField(blank=True, choices=[('Scan', 'Scan'), ('Print', 'Print'), ('Photocopy', 'Photocopy')], max_length=10, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_printer.modelprinter')),
            ],
        ),
    ]
