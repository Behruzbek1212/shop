# Generated by Django 4.2.5 on 2023-09-12 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=500)),
                ('narxi', models.IntegerField()),
                ('rasm1', models.ImageField(default='10', upload_to='media/')),
            ],
        ),
    ]