# Generated by Django 4.0.2 on 2022-02-17 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_rename_otp_generateotp'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='producthasoffer',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='producthasoffer',
            name='offer_id',
        ),
        migrations.RemoveField(
            model_name='producthasoffer',
            name='product_id',
        ),
        migrations.RemoveField(
            model_name='sales',
            name='offer_id',
        ),
        migrations.DeleteModel(
            name='Offer',
        ),
        migrations.DeleteModel(
            name='productHasOffer',
        ),
    ]