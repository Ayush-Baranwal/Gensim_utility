# Generated by Django 3.1.6 on 2021-03-04 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gensimutility', '0002_auto_20210304_0836'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='written_by',
            field=models.CharField(default='admin', max_length=30),
            preserve_default=False,
        ),
    ]