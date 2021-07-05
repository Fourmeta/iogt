# Generated by Django 3.1.12 on 2021-06-24 12:52

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0005_auto_20210615_0842'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='rapid_pro_message_id',
            new_name='rapidpro_message_id',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='content',
            new_name='text',
        ),
        migrations.RemoveField(
            model_name='chatbotchannel',
            name='identifier',
        ),
        migrations.RemoveField(
            model_name='message',
            name='attachments',
        ),
        migrations.RemoveField(
            model_name='message',
            name='sent_from_bot',
        ),
        migrations.RemoveField(
            model_name='userthread',
            name='deleted',
        ),
        migrations.RemoveField(
            model_name='userthread',
            name='unread',
        ),
        migrations.AddField(
            model_name='thread',
            name='last_message_at',
            field=models.DateTimeField(default=None, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='userthread',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='userthread',
            name='is_read',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='message',
            name='quick_replies',
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name='message',
            name='sent_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='thread',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='userthread',
            name='thread',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_threads', to='messaging.thread'),
        ),
    ]
