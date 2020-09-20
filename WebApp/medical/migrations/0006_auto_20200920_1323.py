# Generated by Django 3.0.7 on 2020-09-20 11:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('medical', '0005_auto_20200920_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pacjent',
            name='plec',
            field=models.CharField(choices=[('K', 'k'), ('M', 'm')], max_length=1),
        ),
        migrations.AlterField(
            model_name='pacjent',
            name='rok_urodzenia',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pacjent',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
