# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='member',
            field=models.ForeignKey(related_name='books', to='library.Member', null=True),
        ),
    ]
