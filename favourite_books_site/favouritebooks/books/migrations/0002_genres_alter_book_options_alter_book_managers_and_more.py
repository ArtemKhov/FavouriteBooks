# Generated by Django 5.1.1 on 2024-10-06 18:18

import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['-time_create']},
        ),
        migrations.AlterModelManagers(
            name='book',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='is_published',
            field=models.BooleanField(choices=[(0, 'Draft'), (1, 'Published')], default=0),
        ),
        migrations.AddIndex(
            model_name='book',
            index=models.Index(fields=['-time_create'], name='books_book_time_cr_d8b845_idx'),
        ),
    ]
