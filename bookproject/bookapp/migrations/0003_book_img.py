# Generated by Django 4.2.3 on 2023-07-17 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0002_book_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='img',
            field=models.ImageField(default=2, upload_to='gallery'),
            preserve_default=False,
        ),
    ]
