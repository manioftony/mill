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







































