# Generated by Django 4.0.4 on 2022-04-23 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0003_alter_offer_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='offer',
            options={'ordering': ('rate_min',)},
        ),
        migrations.RemoveField(
            model_name='offer',
            name='payment',
        ),
    ]