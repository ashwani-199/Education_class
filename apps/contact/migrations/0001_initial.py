# Generated by Django 5.2 on 2025-05-04 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('update_at', models.DateField(auto_now_add=True)),
                ('created_at', models.DateField(auto_now=True)),
            ],
        ),
    ]
