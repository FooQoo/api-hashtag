# Generated by Django 2.2.4 on 2019-08-26 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hashtags', '0005_auto_20190826_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biterm',
            name='biterm_id',
            field=models.CharField(editable=False, max_length=64, primary_key=True, serialize=False),
        ),
        migrations.AlterUniqueTogether(
            name='biterm',
            unique_together=set(),
        ),
    ]