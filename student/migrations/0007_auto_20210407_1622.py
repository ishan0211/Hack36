# Generated by Django 3.1.1 on 2021-04-07 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_delete_following'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='profileImage',
            field=models.ImageField(blank=True, default='teacherImages/def_user.png', upload_to='studentImages'),
        ),
    ]