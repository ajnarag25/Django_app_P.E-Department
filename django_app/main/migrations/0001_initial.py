# Generated by Django 3.2.8 on 2021-11-08 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('course', models.CharField(max_length=200)),
            ],
        ),
    ]