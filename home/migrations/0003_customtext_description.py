# Generated by Django 2.2.14 on 2020-09-07 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_load_initial_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='customtext',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
