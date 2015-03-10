# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cardapio', '0005_cardapio_prep'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dia_cardapio',
            name='data',
            field=models.CharField(max_length=10),
        ),
    ]
