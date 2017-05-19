# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_auto_20170424_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='author',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
