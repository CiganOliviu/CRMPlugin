# Generated by Django 3.0.8 on 2020-10-25 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClientsManagement', '0012_auto_20201024_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientsdetail',
            name='profile_image',
            field=models.ImageField(default='default.jpg', upload_to='clients-profile-images/'),
        ),
    ]
