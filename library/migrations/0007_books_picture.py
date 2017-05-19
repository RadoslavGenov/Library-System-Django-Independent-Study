# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_remove_books_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='picture',
            field=models.ImageField(upload_to=b'', blank=True),
        ),
    ]
