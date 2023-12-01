# Generated by Django 4.2.6 on 2023-11-10 07:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api_auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Officer',
            fields=[
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=10)),
                ('officerID', models.CharField(max_length=10, unique=True)),
                ('position', models.CharField(default='Officer', max_length=30)),
            ],
            options={
                'db_table': 'officier_info',
                'ordering': ['user_id'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=10)),
                ('studentID', models.CharField(max_length=10)),
                ('major', models.IntegerField(choices=[(1, 'Khoa học và kỹ thuật máy tính'), (2, 'Quản lý công nghiệp')], default=1)),
            ],
            options={
                'db_table': 'student_info',
                'ordering': ['user_id'],
                'abstract': False,
            },
        ),
    ]
