# Generated by Django 4.1.3 on 2022-11-03 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('encoder', '0004_alter_rot_amount'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rot',
            options={'ordering': ['-usages'], 'verbose_name': 'Rot', 'verbose_name_plural': 'Rots'},
        ),
        migrations.RenameField(
            model_name='rot',
            old_name='amount',
            new_name='usages',
        ),
    ]
