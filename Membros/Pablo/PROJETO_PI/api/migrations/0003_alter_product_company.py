# Generated by Django 5.0.3 on 2024-05-01 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_product_cnpj_alter_product_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='company',
            field=models.CharField(max_length=101),
        ),
    ]
