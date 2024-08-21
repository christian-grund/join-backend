# Generated by Django 5.0.7 on 2024-08-21 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_remove_taskitem_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mail', models.CharField(max_length=100)),
                ('phone', models.DecimalField(decimal_places=0, max_digits=20)),
                ('color', models.CharField(max_length=100)),
                ('isChoosen', models.BooleanField(default=False)),
            ],
        ),
    ]