# Generated by Django 3.1.5 on 2021-01-25 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('text', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='blog_images/%Y/%m/%d/')),
            ],
        ),
    ]
