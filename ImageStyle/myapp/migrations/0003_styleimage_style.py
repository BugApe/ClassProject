# Generated by Django 2.2.5 on 2019-10-16 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20191016_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='styleimage',
            name='style',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]
