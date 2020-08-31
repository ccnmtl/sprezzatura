# Generated by Django 2.2.14 on 2020-07-24 04:56

from django.db import migrations
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20200724_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicpage',
            name='body',
            field=wagtail.core.fields.StreamField([('rich_text', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.core.blocks.StructBlock([('image_file', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title', wagtail.core.blocks.CharBlock(help_text='Title for the image', required=False)), ('caption', wagtail.core.blocks.CharBlock(help_text='Caption for the image', required=False))]))]),
        ),
        migrations.AlterField(
            model_name='eartrainingelementpage',
            name='body',
            field=wagtail.core.fields.StreamField([('topic', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('musical_elements', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('element_title', wagtail.core.blocks.CharBlock()), ('content', wagtail.core.blocks.StreamBlock([('rich_text', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'ol', 'li', 'hr', 'link', 'document_link'])), ('image', wagtail.core.blocks.StructBlock([('image_file', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title', wagtail.core.blocks.CharBlock(help_text='Title for the image', required=False)), ('caption', wagtail.core.blocks.CharBlock(help_text='Caption for the image', required=False))])), ('video', wagtail.core.blocks.StructBlock([('url', wagtail.core.blocks.URLBlock()), ('description', wagtail.core.blocks.CharBlock(required=False))]))], icon='cogs'))])))]))]),
        ),
        migrations.AlterField(
            model_name='eartraininglevelpage',
            name='body',
            field=wagtail.core.fields.StreamField([('rich_text', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.core.blocks.StructBlock([('image_file', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title', wagtail.core.blocks.CharBlock(help_text='Title for the image', required=False)), ('caption', wagtail.core.blocks.CharBlock(help_text='Caption for the image', required=False))]))]),
        ),
        migrations.AlterField(
            model_name='improvisationcombinationpage',
            name='body',
            field=wagtail.core.fields.StreamField([('rich_text', wagtail.core.blocks.RichTextBlock()), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='main/blocks/table_block.html')), ('image', wagtail.core.blocks.StructBlock([('image_file', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title', wagtail.core.blocks.CharBlock(help_text='Title for the image', required=False)), ('caption', wagtail.core.blocks.CharBlock(help_text='Caption for the image', required=False))]))]),
        ),
        migrations.AlterField(
            model_name='improvisationtypepage',
            name='body',
            field=wagtail.core.fields.StreamField([('rich_text', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.core.blocks.StructBlock([('image_file', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title', wagtail.core.blocks.CharBlock(help_text='Title for the image', required=False)), ('caption', wagtail.core.blocks.CharBlock(help_text='Caption for the image', required=False))]))]),
        ),
    ]