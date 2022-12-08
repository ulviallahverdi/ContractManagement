from random import choices
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField
from sqlalchemy import ForeignKey
from multiselectfield import MultiSelectField

MY_CHOICES = ((1, 'IT'),
              (2, 'Accounting'),
              (3, 'F&B'),
              (4, 'SPA'))

ACCESSES =    ((1, 'Initiator'),
              (2, 'Purchasing'),
              (3, 'Accounting Control'),
              (4, 'DOF'),
              (5, 'GM'))


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    #department = ForeignKey(Department,ondelete=models.DO_NOTHING)
    purchasing_rights = models.BooleanField(verbose_name="Purchasing Rights")
    account_control = models.BooleanField(verbose_name="Accounting Control")
    dof_rights = models.BooleanField(verbose_name="DOF Right")
    gm_rights = models.BooleanField(verbose_name="GM Rights")
    allowed_departments = MultiSelectField(choices=MY_CHOICES)
    def __str__(self):
        return self.user.username