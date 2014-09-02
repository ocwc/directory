# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='user',
            field=models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='general_expertise',
            field=models.ManyToManyField(null=True, to='web.GeneralExpertise', blank=True, verbose_name='Open Education - General'),
        ),
        migrations.AlterField(
            model_name='person',
            name='general_expertise_other',
            field=models.TextField(blank=True, max_length=255, verbose_name='Other, please indicate:'),
        ),
        migrations.AlterField(
            model_name='person',
            name='is_member',
            field=models.CharField(choices=[('0', "Don't know"), ('1', 'Yes'), ('2', 'No')], max_length=10, verbose_name='Open Education Consortium member?'),
        ),
        migrations.AlterField(
            model_name='person',
            name='mooc_expertise',
            field=models.ManyToManyField(null=True, to='web.MOOCExpertise', blank=True, verbose_name='MOOCs'),
        ),
        migrations.AlterField(
            model_name='person',
            name='mooc_expertise_other',
            field=models.TextField(blank=True, verbose_name='Other, please indicate:'),
        ),
        migrations.AlterField(
            model_name='person',
            name='oer_expertise',
            field=models.ManyToManyField(null=True, to='web.OERExpertise', blank=True, verbose_name='Open Educational Resources'),
        ),
        migrations.AlterField(
            model_name='person',
            name='openacess_expertise',
            field=models.ManyToManyField(null=True, to='web.OpenAccessExpertise', blank=True, verbose_name='Open Access'),
        ),
        migrations.AlterField(
            model_name='person',
            name='region',
            field=models.ManyToManyField(to='web.Region', verbose_name='Please select the geographic regions in which you have professional experience:'),
        ),
    ]
