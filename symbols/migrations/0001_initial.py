# Generated by Django 3.2.6 on 2021-08-30 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Symbol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(blank=True, default=None, null=True)),
                ('name', models.CharField(default=None, max_length=100)),
                ('type', models.CharField(default=None, max_length=100)),
                ('size', models.IntegerField(blank=True, default=None, null=True)),
            ],
        ),
    ]
