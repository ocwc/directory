# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('iso_code', models.CharField(max_length=6)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GeneralExpertise',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MOOCExpertise',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OERExpertise',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OpenAccessExpertise',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('alternative_contact', models.CharField(max_length=255, blank=True)),
                ('slug', models.SlugField(max_length=255)),
                ('job_title', models.CharField(max_length=255, blank=True)),
                ('institution', models.CharField(max_length=255, blank=True)),
                ('is_member', models.CharField(choices=[(0, "Don't know"), (1, 'Yes'), (2, 'No')], max_length=10, verbose_name='Open Education Consortium member?')),
                ('city', models.CharField(max_length=255, blank=True)),
                ('state_province', models.CharField(max_length=255, blank=True)),
                ('language_native', models.TextField(blank=True, verbose_name='Native/near native level')),
                ('language_business', models.TextField(blank=True, verbose_name='Business level')),
                ('language_conversational', models.TextField(blank=True, verbose_name='Conversational')),
                ('general_expertise_other', models.TextField(max_length=255, blank=True, verbose_name='Other, please indicate')),
                ('oer_expertise_other', models.TextField(blank=True, verbose_name='Other, please indicate:')),
                ('openacess_expertise_other', models.TextField(blank=True, verbose_name='Other, please indicate:')),
                ('mooc_expertise_other', models.TextField(blank=True)),
                ('discipline', models.TextField(blank=True, verbose_name='If you have expertise with open education in a particular discipline, please indicate:')),
                ('personal_statement', models.TextField(blank=True)),
                ('external_links', models.TextField(blank=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('mod_date', models.DateTimeField(auto_now=True)),
                ('visible', models.BooleanField(default=True)),
                ('country', models.ForeignKey(to='web.Country', null=True)),
                ('general_expertise', models.ManyToManyField(to='web.GeneralExpertise', verbose_name='Open Education - General', null=True)),
                ('mooc_expertise', models.ManyToManyField(to='web.MOOCExpertise', verbose_name='If you have expertise with open education in a particular discipline, please indicate:', null=True)),
                ('oer_expertise', models.ManyToManyField(to='web.OERExpertise', verbose_name='Open Educational Resources', null=True)),
                ('openacess_expertise', models.ManyToManyField(to='web.OpenAccessExpertise', verbose_name='MOOCs', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='person',
            name='region',
            field=models.ManyToManyField(to='web.Region', verbose_name='Please select the geographic regions in which you have professional experience:*'),
            preserve_default=True,
        ),
    ]
