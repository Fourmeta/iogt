# Generated by Django 3.1.12 on 2021-06-08 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_merge_20210603_0534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='allow_comments',
            field=models.BooleanField(default=False),
        ),
    ]
