# Generated by Django 3.2.4 on 2021-08-18 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, default='klasikpp.jpg', null=True, upload_to='', verbose_name='Profil Resmi'),
        ),
    ]
