# Generated by Django 4.2 on 2023-09-16 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_alter_post_ekran_dioganali'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='asosis_kamera',
            new_name='asosiy_kamera',
        ),
    ]