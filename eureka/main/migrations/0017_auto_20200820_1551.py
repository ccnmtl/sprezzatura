# Generated by Django 2.2.14 on 2020-08-20 19:51

from django.db import migrations
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20200820_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eartrainingelementpage',
            name='body',
            field=wagtail.core.fields.StreamField([('rich_text', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'ol', 'hr', 'link', 'document_link'])), ('topic', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=False)), ('musical_elements', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('element_title', wagtail.core.blocks.CharBlock(required=False)), ('content', wagtail.core.blocks.StreamBlock([('rich_text', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document_link'], required=False)), ('image', wagtail.core.blocks.StructBlock([('image_file', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title', wagtail.core.blocks.CharBlock(help_text='Title for the image', required=False)), ('caption', wagtail.core.blocks.CharBlock(help_text='Caption for the image', required=False))], required=False)), ('video', wagtail.core.blocks.StructBlock([('url', wagtail.core.blocks.URLBlock()), ('description', wagtail.core.blocks.CharBlock(required=False))], required=False))], icon='cogs', required=False))]), required=False))]))]),
        ),
        migrations.AlterField(
            model_name='eartraininglevelpage',
            name='body',
            field=wagtail.core.fields.StreamField([('rich_text', wagtail.core.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'ol', 'hr', 'link', 'document-link', 'image', 'embed'])), ('image', wagtail.core.blocks.StructBlock([('image_file', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title', wagtail.core.blocks.CharBlock(help_text='Title for the image', required=False)), ('caption', wagtail.core.blocks.CharBlock(help_text='Caption for the image', required=False))]))]),
        ),
        migrations.AlterField(
            model_name='improvisationcombinationpage',
            name='body',
            field=wagtail.core.fields.StreamField([('rich_text', wagtail.core.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'ol', 'hr', 'link', 'document-link', 'image', 'embed'])), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='main/blocks/table_block.html')), ('image', wagtail.core.blocks.StructBlock([('image_file', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title', wagtail.core.blocks.CharBlock(help_text='Title for the image', required=False)), ('caption', wagtail.core.blocks.CharBlock(help_text='Caption for the image', required=False))]))]),
        ),
        migrations.AlterField(
            model_name='improvisationtypepage',
            name='body',
            field=wagtail.core.fields.StreamField([('rich_text', wagtail.core.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'ol', 'hr', 'link', 'document-link', 'image', 'embed'])), ('image', wagtail.core.blocks.StructBlock([('image_file', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title', wagtail.core.blocks.CharBlock(help_text='Title for the image', required=False)), ('caption', wagtail.core.blocks.CharBlock(help_text='Caption for the image', required=False))]))]),
        ),
    ]