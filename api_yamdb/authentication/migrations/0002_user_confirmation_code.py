# Generated by Django 3.2 on 2022-12-16 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='confirmation_code',
            field=models.CharField(default='123456789', max_length=100, null=True, verbose_name='Код подтверждения'),
        ),
    ]