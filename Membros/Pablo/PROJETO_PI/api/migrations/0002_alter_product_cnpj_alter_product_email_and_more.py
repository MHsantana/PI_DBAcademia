# Generated by Django 5.0.3 on 2024-04-30 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cnpj',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='headquarter',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='maintenance',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='tel',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]