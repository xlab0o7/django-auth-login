# Generated by Django 4.2.7 on 2023-12-07 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fooditems', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fooditems',
            name='uname',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
