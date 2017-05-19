# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_auto_20170425_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='picture',
            field=models.ImageField(upload_to=b'', blank=True),
        ),
    ]
