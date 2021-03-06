# Generated by Django 3.1.7 on 2021-04-19 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=100)),
                ('book_author', models.CharField(max_length=150)),
                ('book_price', models.IntegerField(max_length=20)),
                ('book_cover', models.ImageField(upload_to='')),
            ],
            options={
                'db_table': 'book',
            },
        ),
    ]
