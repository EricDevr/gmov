# Generated by Django 3.2.6 on 2021-09-06 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='static/images')),
                ('title', models.CharField(max_length=500)),
                ('slug', models.SlugField()),
                ('content', models.TextField(max_length=20000)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
