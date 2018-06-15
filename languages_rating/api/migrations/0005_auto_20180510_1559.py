# Generated by Django 2.0.3 on 2018-05-10 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20180509_1936'),
    ]

    operations = [
        migrations.CreateModel(
            name='LanguageData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('popularity', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
        migrations.RemoveField(
            model_name='language',
            name='date',
        ),
        migrations.RemoveField(
            model_name='language',
            name='popularity',
        ),
        migrations.AddField(
            model_name='languagedata',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.Language'),
        ),
    ]