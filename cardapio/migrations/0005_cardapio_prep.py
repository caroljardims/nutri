# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cardapio', '0004_auto_20150310_1554'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cardapio_Prep',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dia', models.ForeignKey(to='cardapio.Dia_Cardapio', to_field='id')),
                ('prep', models.ForeignKey(to='cardapio.Prepara', to_field='id')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
