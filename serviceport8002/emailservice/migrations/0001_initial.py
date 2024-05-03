# Generated by Django 5.0.4 on 2024-05-01 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('sender_username', models.CharField(max_length=100)),
                ('sent_to', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('message', models.CharField(default='  ', max_length=2000)),
                ('is_debug', models.BooleanField(default=True)),
            ],
        ),
    ]
