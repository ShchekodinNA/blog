# Generated by Django 4.1.1 on 2022-09-11 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(null=True, upload_to=None),
        ),
        migrations.AlterField(
            model_name='post',
            name='img_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]