# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cardapio', '0002_prep_alimentos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.DateTimeField()),
                ('prep', models.ForeignKey(to='cardapio.Prepara', to_field='id')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
