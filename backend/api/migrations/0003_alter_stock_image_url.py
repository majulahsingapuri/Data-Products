# Generated by Django 4.1.3 on 2022-11-19 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_content_news_source_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='image_url',
            field=models.URLField(max_length=999, null=True),
        ),
    ]