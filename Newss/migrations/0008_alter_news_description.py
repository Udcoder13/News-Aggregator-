# Generated by Django 4.2 on 2023-08-12 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Newss', '0007_alter_news_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
