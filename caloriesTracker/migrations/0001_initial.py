# Generated by Django 4.2.7 on 2023-12-06 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fooditems', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tracker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemname', models.CharField(max_length=50)),
                ('user_calories', models.IntegerField()),
                ('total_cal_day', models.IntegerField()),
                ('status', models.BooleanField()),
                ('fooditems', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fooditems.fooditems')),
            ],
        ),
    ]
