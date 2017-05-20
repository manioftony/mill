from __future__ import division
from django.db import models


# Create your models here.










ACTIVE = ((0,'Inactive'), (2, 'Active'),)
class Base(models.Model):
    
    """ Basic Fields """

    active = models.PositiveIntegerField(choices = ACTIVE, default=2)
    created_on = models.DateTimeField(auto_now_add = True)
    modified_on = models.DateTimeField(auto_now = True)

    def switch(self):
        self.active = {0: 2, 2: 0}[self.active]
        self.save()
        return self.active

    class Meta:
        abstract = True



class OrgInfo(Base):
    customer_name = models.CharField(max_length=200,blank=True, null=True)
    customer_created = models.DateField(blank=True, null=True)
    no_of_profile  = models.IntegerField(blank=True,null=True)
    no_of_donation = models.IntegerField(blank=True,null=True)
    total_amount = models.IntegerField(blank=True,null=True)
    sub_domain = models.CharField(max_length=200,blank=True,null=True)
    def __unicode__(self):
        return self.customer_name






class Profile(Base):

    ACTIVE_CHOICES = ((0, 'Male'), (2, 'Female'),)

    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    gender = models.PositiveIntegerField(
        choices=ACTIVE_CHOICES, blank=True, null=True)
    blood_group = models.CharField(max_length=100, blank=True, null=True)
    current_address = models.CharField(max_length=100, blank=True, null=True)
    permanet_address = models.CharField(max_length=100, blank=True, null=True)
    joining_date = models.DateField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(max_length=100, blank=True, null=True)
    mobile_number = models.IntegerField(blank=True, null=True)
    landline_number = models.IntegerField(blank=True, null=True,)
    voter_id = models.CharField(max_length=100, blank=True, null=True)
    driving_license = models.CharField(max_length=100, blank=True, null=True)
    aadhar_card = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return self.first_name




class EmployeeInfo(Base):
    employee_id = models.CharField(max_length=100, blank=True, null=True)
    working_shift = models.CharField(max_length=100, blank=True, null=True)
    login_time = models.TimeField(blank=True, null=True)
    logout_time = models.TimeField(blank=True, null=True)
    employee_role = models.CharField(max_length=100, blank=True, null=True)
    under_supervision = models.CharField(max_length=100, blank=True, null=True)
    break_time = models.TimeField(blank=True, null=True)
    over_time = models.TimeField(blank=True, null=True)
    total_working_hour_per_day = models.IntegerField(blank=True, null=True)
    def __unicode__(self):
        return self.employee_id







class Production(Base):
    kg = models.IntegerField(max_length=100, blank=True, null=True)
    date = models.DateField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return '%s'%(self.kg)

    def total_loss(self):
        # from __future__ import division
        return round((7/100)*self.kg)

    def yarn_output(self):
        return round((93/100)*self.kg)










class Company(Base):

    name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    type_of_company = models.CharField(max_length=100, blank=True, null=True)       
    
    def __unicode__(self):
        return self.name




cur_status = ((0,'open'),(1,'In progress'),(2,'closed'))

class Requirement(Base):
    current_status = models.IntegerField(choices = cur_status, blank = True, null = True)
    company = models.ForeignKey(Company, blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)
    no_openings = models.CharField(max_length=100, blank=True, null=True)
    technology = models.CharField(max_length=100, blank=True, null=True)
    skills = models.CharField(max_length=100, blank=True, null=True)
    experience = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    type_of_opening = models.CharField(max_length=100, blank=True, null=True)
    salary_range = models.CharField(max_length=100, blank=True, null=True)
    unique_id = models.CharField(null=True, max_length=100, unique=True)
    resume = models.FileField(upload_to='static/resume/img/%Y/%m/%d',blank=True, null=True)
    def __unicode__(self):
        return self.position























