# Generated by Django 2.2.5 on 2019-10-19 02:46

from django.db import migrations, models
import system.storage


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20191019_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doodleimage',
            name='image',
            field=models.ImageField(storage=system.storage.ImageStorage(), upload_to='./doodle/samples'),
        ),
    ]
