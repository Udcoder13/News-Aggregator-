# Generated by Django 4.2 on 2023-08-26 00:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Newss', '0010_comments_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='news',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Newss.news'),
        ),
    ]