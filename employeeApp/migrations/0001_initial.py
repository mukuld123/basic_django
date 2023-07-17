# Generated by Django 4.2.3 on 2023-07-13 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('dept', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('joining_date', models.DateField()),
                ('location', models.CharField(max_length=50)),
            ],
        ),
    ]