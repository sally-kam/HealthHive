# Generated by Django 4.2 on 2023-05-14 03:40

from django.db import migrations, models
import storages.backends.s3boto3


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, storage=storages.backends.s3boto3.S3Boto3Storage(), upload_to=''),
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]
