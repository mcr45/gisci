# Generated by Django 4.1.1 on 2022-11-13 02:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='pubblished_date',
            new_name='published_date',
        ),
    ]
