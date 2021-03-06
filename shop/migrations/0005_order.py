# Generated by Django 3.0.8 on 2020-11-15 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20201113_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=5000)),
                ('name', models.CharField(max_length=88)),
                ('email', models.CharField(max_length=88)),
                ('address', models.CharField(max_length=88)),
                ('city', models.CharField(max_length=88)),
                ('state', models.CharField(max_length=88)),
                ('zip_code', models.CharField(max_length=88)),
            ],
        ),
    ]
