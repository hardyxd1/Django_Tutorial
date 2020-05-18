# Generated by Django 3.0.6 on 2020-05-18 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatar/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='employee',
            name='cvitae',
            field=models.ImageField(blank=True, null=True, upload_to='cvitae/%Y/%m/%d'),
        ),
        migrations.AlterModelTable(
            name='employee',
            table='empleado',
        ),
    ]