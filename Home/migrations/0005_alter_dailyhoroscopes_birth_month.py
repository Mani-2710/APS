# Generated by Django 5.0 on 2024-03-09 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_rename_horoscope_dailyhoroscopes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyhoroscopes',
            name='birth_month',
            field=models.TextField(),
        ),
    ]
