# Generated by Django 4.1.1 on 2022-09-16 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_post_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='img_name',
        ),
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, upload_to='blog-img'),
        ),
    ]
