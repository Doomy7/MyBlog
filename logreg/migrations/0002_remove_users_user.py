# Generated by Django 3.0.4 on 2020-03-26 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logreg', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='user',
        ),
    ]
