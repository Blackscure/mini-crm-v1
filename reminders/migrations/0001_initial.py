# Generated by Django 5.1.4 on 2025-01-04 22:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lead', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=255)),
                ('scheduled_time', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_sent', models.BooleanField(default=False)),
                ('lead', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reminders', to='lead.lead')),
            ],
        ),
    ]
