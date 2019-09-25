# Generated by Django 2.0.6 on 2019-09-25 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('pageNumber', models.IntegerField()),
                ('genre', models.CharField(max_length=60)),
                ('publishDate', models.DateField()),
            ],
        ),
    ]