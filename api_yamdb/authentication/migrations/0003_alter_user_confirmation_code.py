# Generated by Django 3.2 on 2022-12-17 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_user_confirmation_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.CharField(default='e5pFwSCJEX0kLc3Kux2Q', max_length=100, null=True, verbose_name='Код подтверждения'),
        ),
    ]