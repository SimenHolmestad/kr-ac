# Generated by Django 2.1.1 on 2018-09-16 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forumpost',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]