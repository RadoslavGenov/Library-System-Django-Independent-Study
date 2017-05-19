# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20170424_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='author',
            field=models.ForeignKey(related_name='books', to='library.Author'),
        ),
    ]
