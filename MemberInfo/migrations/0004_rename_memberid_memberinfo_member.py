# Generated by Django 5.0.4 on 2024-04-26 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MemberInfo', '0003_rename_member_memberinfo_memberid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='memberinfo',
            old_name='memberid',
            new_name='member',
        ),
    ]