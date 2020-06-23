# Generated by Django 2.2.13 on 2020-06-23 16:39

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eartrainingelementpage',
            name='body',
            field=wagtail.core.fields.StreamField([('rich_text', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('music_example', wagtail.core.blocks.StructBlock([('file', wagtail.documents.blocks.DocumentChooserBlock()), ('caption', wagtail.core.blocks.CharBlock(required=False))]))]),
        ),
    ]
