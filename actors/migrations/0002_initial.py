# Generated by Django 4.2.1 on 2024-05-09 13:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('actors', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='author',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='actor',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='actors.category', verbose_name='Категории'),
        ),
        migrations.AddField(
            model_name='actor',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tags', to='actors.tagpost', verbose_name='Теги'),
        ),
        migrations.AddIndex(
            model_name='actor',
            index=models.Index(fields=['-time_create'], name='actors_acto_time_cr_46e916_idx'),
        ),
    ]