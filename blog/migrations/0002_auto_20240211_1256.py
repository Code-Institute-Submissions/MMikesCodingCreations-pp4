# Generated by Django 3.2.24 on 2024-02-11 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'post', 'verbose_name_plural': 'posts'},
        ),
        migrations.RenameField(
            model_name='category',
            old_name='Category_name',
            new_name='category_name',
        ),
    ]