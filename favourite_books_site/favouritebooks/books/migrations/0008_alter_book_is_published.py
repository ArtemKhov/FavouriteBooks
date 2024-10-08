# Generated by Django 5.1.1 on 2024-10-09 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_alter_book_is_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='is_published',
            field=models.BooleanField(choices=[(1, 'Published'), (0, 'Draft')], default=1),
        ),
    ]
