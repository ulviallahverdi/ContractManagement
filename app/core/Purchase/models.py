from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField

class ContractType(models.Model):
    name = models.CharField(verbose_name="Contract Type",max_length=50)

    def __str__(self):
        return self.name

class PaymentTerms(models.Model):
    name = models.CharField(verbose_name="Payment Terms",max_length=100)

    def __str__(self):
        return self.name

class TerminationTerms(models.Model):
    name = models.CharField(verbose_name="Termination Terms",max_length=100)

    def __str__(self):
        return self.name

class Currency(models.Model):
    name = models.CharField(max_length=10,verbose_name="Currency")

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=60,verbose_name="Department Name")
    count = models.IntegerField(verbose_name="Count")

    def __str__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(verbose_name="Contract Status",max_length=20)

    def __str__(self):
        return self.name

# Create your models here.
class Contract(models.Model):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    vendor_code = models.CharField(verbose_name="Vendor Code",max_length=10)
    contract_type = models.ForeignKey(ContractType,on_delete=models.DO_NOTHING)
    contract_id = models.CharField(max_length=10, verbose_name="Contract ID",primary_key=True,null=False)
    start_date = models.DateTimeField(auto_now_add=True,verbose_name="Start Date")
    end_date = models.DateTimeField(verbose_name="End Date")
    description = models.CharField(verbose_name="Description",max_length=200,null=True,blank=True)
    payment_terms = models.ForeignKey(PaymentTerms,on_delete=models.DO_NOTHING)
    termination_terms = models.ForeignKey(TerminationTerms,on_delete=models.DO_NOTHING)
    status = models.ForeignKey(Status,on_delete=models.DO_NOTHING)
    hod_comments = models.CharField(verbose_name="HOD Comments",max_length=200,null=True,blank=True)
    account_number = models.IntegerField(verbose_name="Acccount Number",null=True,blank=True)
    currency = models.ForeignKey(Currency,on_delete=models.DO_NOTHING)
    approval_status = models.IntegerField(verbose_name="Approval Status",default=0)
    contract_value = models.IntegerField(verbose_name="Contract Value")
    percentage = models.IntegerField(verbose_name="Contract Percentage")
    department = models.ForeignKey(Department,on_delete=models.DO_NOTHING)
    vendor_email = models.EmailField(verbose_name="Vendor Email",max_length=80)
    vendor_phone = models.CharField(verbose_name="Vendor Phone",max_length=40)
    vendor_director = models.CharField(verbose_name="Vendor Director",max_length=40)
    vendor_name = models.CharField(verbose_name="Vendor Name",max_length=40)
    vendor_voen = models.IntegerField(verbose_name="Vendor VÖEN",null=True,blank=True,default=False)
    vendor_address = models.CharField(verbose_name="Vendor Address",max_length=40,null=True,blank=True,default=False)
    bank_name = models.CharField(verbose_name="Bank Name",max_length=20,null=True,blank=True,default=False)
    bank_voen = models.CharField(verbose_name="Bank VOEN",max_length=20,null=True,blank=True,default=False)
    bank_code = models.CharField(verbose_name="Bank Code",max_length=20,null=True,blank=True,default=False)
    bank_swift = models.CharField(verbose_name="Bank SWIFT",max_length=30,null=True,blank=True,default=False)
    bank_m_h = models.CharField(verbose_name="Bank Müxbir Hesab",max_length=30,null=True,blank=True,default=False)
    bank_h_h = models.CharField(verbose_name="Bank Hesablaşma Hesabı",max_length=30,null=True,blank=True,default=False)
    contract_exported_link = models.CharField(verbose_name="Link",max_length=300,null=True,blank=True)
    creator_edit = models.BooleanField(verbose_name="Initiator can edit", default=True)
    reject_comment = models.CharField(max_length=300, verbose_name="Rejection Comment",null=True,blank=True)

    



    

    def __str__(self):
        return self.contract_id



