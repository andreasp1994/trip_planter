# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tripPlanterApp', '0003_auto_20160313_1936'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='rating',
            field=models.CharField(default=b'No rating', max_length=5),
            preserve_default=True,
        ),
    ]
