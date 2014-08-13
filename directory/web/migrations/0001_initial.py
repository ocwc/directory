# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('street_address', models.CharField(max_length=255, blank=True)),
                ('street_address2', models.CharField(max_length=255, blank=True)),
                ('city', models.CharField(max_length=255, blank=True)),
                ('state_province', models.CharField(max_length=255, blank=True)),
                ('zip_postal', models.CharField(max_length=255, blank=True)),
                ('country', models.CharField(max_length=255, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GeneralExpertise',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MOOCExpertise',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OERExpertise',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OpenAccessExpertise',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255)),
                ('job_title', models.CharField(max_length=255, blank=True)),
                ('institution', models.CharField(max_length=255, blank=True)),
                ('is_member', models.NullBooleanField(default=None)),
                ('email', models.CharField(max_length=255)),
                ('alternative_contact', models.CharField(max_length=255, blank=True)),
                ('language_native', models.TextField(blank=True)),
                ('language_business', models.TextField(blank=True)),
                ('language_conversational', models.TextField(blank=True)),
                ('general_expertise_other', models.TextField(max_length=255, blank=True)),
                ('oer_expertise_other', models.TextField(blank=True)),
                ('openacess_expertise_other', models.TextField(blank=True)),
                ('mooc_expertise_other', models.TextField(blank=True)),
                ('discipline', models.TextField(blank=True)),
                ('personal_statement', models.TextField(blank=True)),
                ('external_links', models.TextField(blank=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('mod_date', models.DateTimeField(auto_now=True)),
                ('address', models.ForeignKey(to='web.Address', null=True)),
                ('general_expertise', models.ManyToManyField(to='web.GeneralExpertise', null=True)),
                ('mooc_expertise', models.ManyToManyField(to='web.MOOCExpertise', null=True)),
                ('oer_expertise', models.ManyToManyField(to='web.OERExpertise', null=True)),
                ('openacess_expertise', models.ManyToManyField(to='web.OpenAccessExpertise', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='person',
            name='region',
            field=models.ManyToManyField(to='web.Region'),
            preserve_default=True,
        ),
    ]
