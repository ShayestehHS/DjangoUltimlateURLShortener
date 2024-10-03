# Generated by Django 5.0.8 on 2024-09-30 07:02

import django.db.models.deletion
import utils.validators
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urls', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='token',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='url',
            name='url',
            field=models.URLField(max_length=255, validators=[utils.validators.is_https]),
        ),
        migrations.CreateModel(
            name='UrlClick',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True)),
                ('url', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='click', to='urls.url')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_click', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]