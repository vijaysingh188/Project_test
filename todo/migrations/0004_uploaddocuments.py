# Generated by Django 3.1.1 on 2021-06-26 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20200926_1410'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadDocuments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploadfiles', models.FileField(blank=True, null=True, upload_to='media')),
                ('created_at', models.DateField(auto_now=True)),
                ('filename', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
