# Generated by Django 5.0.7 on 2024-08-21 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0005_contactitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactitem',
            name='nr',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=100),
            preserve_default=False,
        ),
    ]