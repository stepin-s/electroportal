# Generated by Django 2.2.14 on 2020-08-14 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0008_auto_20200813_0839'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='upload',
            field=models.FileField(default=0, upload_to='uploads/%Y/%m/%d/'),
            preserve_default=False,
        ),
    ]