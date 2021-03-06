# Generated by Django 3.1.5 on 2021-01-17 11:37

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
            name='blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bimg', models.ImageField(upload_to='pics')),
                ('date', models.DateField()),
                ('post', models.CharField(max_length=100)),
                ('bname', models.CharField(max_length=100)),
                ('bdesc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='travell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dob', models.DateField()),
                ('mobile', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('gender', models.CharField(max_length=20)),
                ('nationality', models.CharField(max_length=50)),
                ('image', models.FileField(null=True, upload_to='pics')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
