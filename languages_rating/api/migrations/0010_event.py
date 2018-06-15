# Generated by Django 2.0.6 on 2018-06-15 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_remove_language_offset'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('year', models.IntegerField()),
                ('month', models.IntegerField()),
            ],
        ),
    ]