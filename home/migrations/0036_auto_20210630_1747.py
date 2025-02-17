# Generated by Django 3.1.12 on 2021-06-30 17:47

from django.db import migrations
import home.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
import wagtailmarkdown.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0035_merge_20210630_1728'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='new_featured_content',
        ),
        migrations.AddField(
            model_name='homepage',
            name='home_featured_content',
            field=wagtail.core.fields.StreamField([('page_button', wagtail.core.blocks.StructBlock([('page', wagtail.core.blocks.PageChooserBlock()), ('text', wagtail.core.blocks.CharBlock(max_length=255, required=False))])), ('embedded_poll', home.blocks.EmbeddedQuestionnaireChooserBlock(page_type=['questionnaires.Poll'])), ('embedded_survey', home.blocks.EmbeddedQuestionnaireChooserBlock(page_type=['questionnaires.Survey'])), ('embedded_quiz', home.blocks.EmbeddedQuestionnaireChooserBlock(page_type=['questionnaires.Quiz'])), ('article', wagtail.core.blocks.PageChooserBlock(page_type=['home.Article']))], null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='body',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(form_classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('markdown', wagtailmarkdown.blocks.MarkdownBlock(icon='code')), ('image', wagtail.images.blocks.ImageChooserBlock()), ('list', wagtail.core.blocks.ListBlock(wagtail.core.blocks.CharBlock(label='Item'))), ('numbered_list', wagtail.core.blocks.ListBlock(wagtail.core.blocks.CharBlock(label='Item'))), ('page_button', wagtail.core.blocks.StructBlock([('page', wagtail.core.blocks.PageChooserBlock()), ('text', wagtail.core.blocks.CharBlock(max_length=255, required=False))])), ('embedded_poll', home.blocks.EmbeddedQuestionnaireChooserBlock(page_type=['questionnaires.Poll'])), ('embedded_survey', home.blocks.EmbeddedQuestionnaireChooserBlock(page_type=['questionnaires.Survey'])), ('embedded_quiz', home.blocks.EmbeddedQuestionnaireChooserBlock(page_type=['questionnaires.Quiz'])), ('media', home.blocks.MediaBlock(icon='media'))]),
        ),
    ]
