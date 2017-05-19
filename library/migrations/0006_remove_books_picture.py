# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_books_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='picture',
        ),
    ]
