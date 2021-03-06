# Generated by Django 3.0.3 on 2020-02-14 08:35

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactTB',
            fields=[
                ('ContactTB_ID', models.AutoField(primary_key=True, serialize=False)),
                ('ContactTB_FirstName', models.CharField(max_length=50)),
                ('ContactTB_LastName', models.CharField(max_length=50)),
                ('ContactTB_EmailtName', models.CharField(max_length=100)),
                ('ContactTB_Designation', models.CharField(max_length=100)),
                ('ContactTB_PhoneName', models.CharField(max_length=50)),
                ('ContactTB_Internal', models.BooleanField(default=False)),
                ('ContactTB_OPSupport', models.BooleanField(default=False)),
                ('ContactTB_DCSupport', models.BooleanField(default=False)),
                ('ContactTB_LastModifiedDt', models.DateTimeField(default=datetime.datetime(2020, 2, 14, 8, 35, 15, 837, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='DecommissionTB',
            fields=[
                ('DecommissionTB_RITM', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('DecommissionTB_By', models.CharField(max_length=100)),
                ('DecommissionTB_LastModifiedDt', models.DateTimeField(default=datetime.datetime(2020, 2, 14, 8, 35, 15, 499, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='InventoryTB',
            fields=[
                ('InventoryTB_ID', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('InventoryTB_Country', models.CharField(max_length=100)),
                ('InventoryTB_Location', models.CharField(max_length=100)),
                ('InventoryTB_LastModifedDt', models.DateTimeField(default=datetime.datetime(2020, 2, 14, 8, 35, 15, 1193, tzinfo=utc))),
                ('InventoryTB_Active', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inv.DecommissionTB')),
                ('InventoryTB_PrimContID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inv.ContactTB', verbose_name='ContactTB_ID')),
            ],
        ),
        migrations.CreateModel(
            name='IPAddTB',
            fields=[
                ('IPAddTB_ID', models.AutoField(primary_key=True, serialize=False)),
                ('IPAddTB_Address', models.CharField(max_length=25)),
                ('IPAddTB_VIP', models.BooleanField(default=False)),
                ('IPAddTB_Purpose', models.CharField(max_length=100)),
                ('IPAddTB_LastModifiedDt', models.DateTimeField(default=datetime.datetime(2020, 2, 14, 8, 35, 15, 1621, tzinfo=utc))),
                ('IPAddTB_InvID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inv.InventoryTB', verbose_name='InventoryTB_ID')),
            ],
        ),
    ]
