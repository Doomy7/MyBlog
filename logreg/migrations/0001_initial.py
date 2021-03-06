# Generated by Django 3.0.4 on 2020-03-26 14:26

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
            name='articles',
            fields=[
                ('aid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('details', models.CharField(max_length=1000)),
                ('category', models.CharField(max_length=30)),
                ('likesNo', models.IntegerField()),
                ('commentsNo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=100)),
                ('dob', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=20)),
                ('interests', models.CharField(max_length=50)),
                ('bio', models.CharField(max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=100)),
                ('aid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logreg.articles')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logreg.users')),
            ],
        ),
        migrations.CreateModel(
            name='likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logreg.articles')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logreg.users')),
            ],
            options={
                'unique_together': {('aid', 'uid')},
            },
        ),
    ]
