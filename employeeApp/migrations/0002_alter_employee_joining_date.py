# Generated by Django 4.2.3 on 2023-07-31 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='joining_date',
            field=models.DateField(blank=True),
        ),
    ]
