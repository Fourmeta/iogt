# Generated by Django 3.1.12 on 2021-06-29 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_merge_20210629_0821'),
        ('iogt_users', '0002_auto_20210624_0739'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='read_articles',
            field=models.ManyToManyField(to='home.Article'),
        ),
    ]
