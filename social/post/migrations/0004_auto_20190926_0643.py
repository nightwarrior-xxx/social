# Generated by Django 2.2.5 on 2019-09-26 06:43

from django.db import migrations, models
import post.models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20190926_0642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=post.models.image_upload),
        ),
    ]
