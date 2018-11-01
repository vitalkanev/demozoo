# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-10-06 21:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productions', '0009_search_document_noneditable'),
    ]

    operations = [
        migrations.AddField(
            model_name='productionlink',
            name='source',
            field=models.CharField(blank=True, editable=False, help_text=b'Identifier to indicate where this link came from - e.g. manual (entered via form), match, auto', max_length=32),
        ),
    ]