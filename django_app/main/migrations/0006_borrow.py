# Generated by Django 3.2.8 on 2021-11-13 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_reserve'),
    ]

    operations = [
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idnum', models.CharField(max_length=100)),
                ('fullname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=100)),
                ('strand', models.CharField(max_length=100)),
                ('items', models.CharField(max_length=100)),
                ('quantity', models.CharField(max_length=100)),
                ('itemfind', models.CharField(max_length=100)),
                ('dateofborrow', models.CharField(max_length=100)),
                ('dateofreturn', models.CharField(max_length=100)),
            ],
        ),
    ]
