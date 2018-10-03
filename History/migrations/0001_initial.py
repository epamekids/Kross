# Generated by Django 2.1 on 2018-10-01 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('text', models.TextField()),
                ('date', models.DateTimeField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
