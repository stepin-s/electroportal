# Generated by Django 2.2.14 on 2020-08-13 05:39

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0007_auto_20200812_0841'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['created_date'], 'verbose_name_plural': 'News'},
        ),
        migrations.AlterModelOptions(
            name='videos',
            options={'ordering': ['created_date'], 'verbose_name_plural': 'Videos'},
        ),
        migrations.AlterField(
            model_name='news',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
