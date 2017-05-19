# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0011_auto_20170429_0722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='picture',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
