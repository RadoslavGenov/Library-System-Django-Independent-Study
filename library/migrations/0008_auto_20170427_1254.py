# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_books_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='picture',
            field=models.ImageField(upload_to='/media/', blank=True),
        ),
    ]
