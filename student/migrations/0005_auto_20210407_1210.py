# Generated by Django 3.1.1 on 2021-04-07 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0010_auto_20210404_1546'),
        ('student', '0004_followed'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Followed',
            new_name='Following',
        ),
    ]