# Generated by Django 4.2 on 2023-08-17 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Newss', '0008_alter_news_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]