# Generated by Django 4.0.1 on 2022-04-23 13:19

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_alter_account_access'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='access',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(1, 'Initiator'), (2, 'Purchasing'), (3, 'Accounting Control'), (4, 'DOF'), (5, 'GM')], max_length=9),
        ),
    ]
