# Generated by Django 5.0.6 on 2024-05-29 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0004_car_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='appartment',
            new_name='appartment_no',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='doors_count',
            new_name='dors_count',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='gearbox_types',
            new_name='gearbox_type',
        ),
        migrations.AlterField(
            model_name='car',
            name='seats_count',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='identity_document_type',
            field=models.CharField(choices=[('dowod', 'dowód osobisty'), ('paszport', 'paszport'), ('prawo_jazdy', 'prawo jazdy')], max_length=20),
        ),
    ]
