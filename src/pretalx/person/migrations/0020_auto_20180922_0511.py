# Generated by Django 2.0.8 on 2018-09-22 10:11

from django.db import migrations, models
import i18nfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0019_auto_20180821_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speakerinformation',
            name='text',
            field=i18nfield.fields.I18nTextField(help_text='You can use <a href="https://docs.pretalx.org/en/latest/user/markdown.html" target="_blank" rel="noopener">Markdown</a> here.', verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='speakerprofile',
            name='biography',
            field=models.TextField(blank=True, help_text='You can use <a href="https://docs.pretalx.org/en/latest/user/markdown.html" target="_blank" rel="noopener">Markdown</a> here.', null=True, verbose_name='Biography'),
        ),
    ]
