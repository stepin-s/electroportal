# Generated by Django 2.2.14 on 2020-08-11 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_videos'),
    ]

    operations = [
        migrations.AddField(
            model_name='videos',
            name='link',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
