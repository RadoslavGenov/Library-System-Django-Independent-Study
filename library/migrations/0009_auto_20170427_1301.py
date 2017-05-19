# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_auto_20170427_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='picture',
            field=models.ImageField(upload_to='images/', blank=True),
        ),
    ]
