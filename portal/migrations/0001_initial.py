# Generated by Django 2.2.2 on 2019-06-08 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=13)),
                ('name', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('birth_date', models.DateTimeField(blank=True, null=True)),
                ('address', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200)),
                ('salary', models.CharField(max_length=200)),
            ],
        ),
    ]
