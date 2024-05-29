# Generated by Django 5.0.2 on 2024-04-16 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discovery', '0002_author_second_name_alter_author_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='info',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='second_name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Отчество'),
        ),
    ]