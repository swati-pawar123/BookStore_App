# Generated by Django 3.1.7 on 2021-04-19 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='book_author',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='book_cover',
            new_name='cover',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='book_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='book_price',
            new_name='price',
        ),
    ]
