# Generated by Django 3.0.6 on 2020-05-20 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fashionmen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('img', models.ImageField(upload_to='Pics')),
            ],
        ),
    ]
