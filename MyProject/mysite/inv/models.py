from django.db import models
from django.utils import timezone

# Create your models here.


class DecommissionTB(models.Model):
    DecommissionTB_RITM = models.CharField(max_length=15, primary_key=True)
    DecommissionTB_By = models.CharField(max_length=100)
    DecommissionTB_LastModifiedDt = models.DateTimeField(default=timezone.now)

class ContactTB(models.Model):
    ContactTB_ID = models.AutoField(primary_key=True)
    ContactTB_FirstName = models.CharField(max_length=50)
    ContactTB_LastName = models.CharField(max_length=50)
    ContactTB_EmailtName = models.CharField(max_length=100)
    ContactTB_Designation = models.CharField(max_length=100)
    ContactTB_PhoneName = models.CharField(max_length=50)
    ContactTB_Internal = models.BooleanField(default=False)
    ContactTB_OPSupport = models.BooleanField(default=False)
    ContactTB_DCSupport = models.BooleanField(default=False)
    ContactTB_LastModifiedDt = models.DateTimeField(default=timezone.now)

class InventoryTB(models.Model):
    InventoryTB_ID = models.CharField(max_length=50, primary_key=True)
    InventoryTB_Country = models.CharField(max_length=100)
    InventoryTB_Location = models.CharField(max_length=100)
    InventoryTB_Active = models.ForeignKey(DecommissionTB, on_delete = models.SET_NULL, blank=True,null=True)
    InventoryTB_PrimContID = models.ForeignKey(ContactTB, on_delete=models.CASCADE,verbose_name='ContactTB_ID')
    #InventoryTB_SecContID = models.ForeignKey(ContactTB, on_delete=models.CASCADE,verbose_name='ContactTB_ID')
    #InventoryTB_SuppID = models.ForeignKey(SupportTB, on_delete=CASCADE)
    #InventoryTB_POID = models.ForeignKey(POTB, on_delete=CASCADE)
    #InventoryTB_AssetID = models.ForeignKey(AssetTB, on_delete=CASCADE)
    InventoryTB_LastModifedDt = models.DateTimeField(default=timezone.now)

class IPAddTB(models.Model):
    IPAddTB_ID = models.AutoField(primary_key=True)
    IPAddTB_InvID = models.ForeignKey(InventoryTB,on_delete=models.CASCADE,verbose_name='InventoryTB_ID')
    IPAddTB_Address = models.CharField(max_length=25)
    IPAddTB_VIP = models.BooleanField(default=False)
    IPAddTB_Purpose = models.CharField(max_length=100)
    IPAddTB_LastModifiedDt = models.DateTimeField(default=timezone.now)