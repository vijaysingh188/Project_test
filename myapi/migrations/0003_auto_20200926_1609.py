# Generated by Django 3.1.1 on 2020-09-26 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_auto_20200926_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='description',
            field=models.TextField(),
        ),
    ]
