# Generated by Django 3.1.12 on 2021-06-22 11:10

from django.db import migrations
import home.blocks
import messaging.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
import wagtailmarkdown.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_merge_20210617_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='body',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(form_classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('markdown', wagtailmarkdown.blocks.MarkdownBlock(icon='code')), ('image', wagtail.images.blocks.ImageChooserBlock()), ('list', wagtail.core.blocks.ListBlock(wagtail.core.blocks.CharBlock(label='Item'))), ('numbered_list', wagtail.core.blocks.ListBlock(wagtail.core.blocks.CharBlock(label='Item'))), ('page', wagtail.core.blocks.PageChooserBlock()), ('media', home.blocks.MediaBlock(icon='media')), ('chat_bot', wagtail.core.blocks.StructBlock([('subject', wagtail.core.blocks.CharBlock()), ('button_text', wagtail.core.blocks.CharBlock()), ('trigger_string', wagtail.core.blocks.CharBlock()), ('channel', messaging.blocks.ChatBotChannelChooserBlock())]))]),
        ),
    ]
