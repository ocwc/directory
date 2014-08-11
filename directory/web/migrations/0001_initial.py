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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('street_address', models.CharField(blank=True, max_length=255)),
                ('street_address2', models.CharField(blank=True, max_length=255)),
                ('city', models.CharField(blank=True, max_length=255)),
                ('state_province', models.CharField(blank=True, max_length=255)),
                ('zip_postal', models.CharField(blank=True, max_length=255)),
                ('country', models.CharField(blank=True, max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GeneralExpertise',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MOOCExpertise',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OERExpertise',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OpenAccessExpertise',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('job_title', models.CharField(blank=True, max_length=255)),
                ('institution', models.CharField(blank=True, max_length=255)),
                ('is_member', models.NullBooleanField(default=None)),
                ('email', models.CharField(max_length=255)),
                ('alternative_contact', models.CharField(blank=True, max_length=255)),
                ('language_native', models.TextField(blank=True)),
                ('language_business', models.TextField(blank=True)),
                ('language_conversational', models.TextField(blank=True)),
                ('general_expertise_other', models.TextField(blank=True, max_length=255)),
                ('oer_expertise_other', models.TextField(blank=True)),
                ('openacess_expertise_other', models.TextField(blank=True)),
                ('mooc_expertise_other', models.TextField(blank=True)),
                ('discipline', models.TextField(blank=True)),
                ('personal_statement', models.TextField(blank=True)),
                ('external_links', models.TextField(blank=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('mod_date', models.DateTimeField(auto_now=True)),
                ('address', models.ForeignKey(null=True, to='web.Address')),
                ('general_expertise', models.ManyToManyField(null=True, to='web.GeneralExpertise')),
                ('mooc_expertise', models.ManyToManyField(null=True, to='web.MOOCExpertise')),
                ('oer_expertise', models.ManyToManyField(null=True, to='web.OERExpertise')),
                ('openacess_expertise', models.ManyToManyField(null=True, to='web.OpenAccessExpertise')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
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
