# Generated by Django 2.2 on 2021-07-22 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorite_food', models.CharField(max_length=255)),
                ('favorite_color', models.CharField(max_length=255)),
            ],
        ),
    ]