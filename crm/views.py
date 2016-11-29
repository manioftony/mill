from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from crm.models import *
import requests
import json

# Create your views here.



def home(request):
    r1 = requests.get('http://tester.dsdemo.mahiti.org/orginfo-list/')
    r1 = eval(r1.content)
    r2 = requests.get('http://developer.dsdemo.mahiti.org/orginfo-list/')
    r2= eval(r2.content)
    r3 = requests.get('http://mc.dsdemo.mahiti.org/orginfo-list/')
    r3= eval(r3.content)
    r4 = requests.get('http://mahiti.dsdemo.mahiti.org/orginfo-list/')
    r4= eval(r4.content)
    

    object_list = OrgInfo.objects.filter(active=2)
    return render(request,'report.html',locals())
  #  return render_to_response("report.html", {"obj_as_json": json.dumps(r1)})


def org_list(request):
    object_list = OrgInfo.objects.filter(active=2)
    return render(request,'orginfo/list.html',locals())



def sales(request):
    return render(request,'orginfo/sales.html',locals())


def company_list(request):
    return render(request,'orginfo/company_list.html',locals())



def get_current_info():
    return [eval(requests.get('http://%s.dsdemo.mahiti.org/orginfo-list/' % i).content)
            for i in ['mahiti', 'developer', 'tester','mc']]

def update_org_info():
    OrgInfo.objects.all().delete()
    org_info = get_current_info()
    for i in range(len(org_info)):
        OrgInfo.objects.create(customer_name = org_info[i]['orgname'],
                                no_of_profile = org_info[i]['proinfo'],
                                no_of_donation = org_info[i]['doninfo'],
                                total_amount = float(org_info[i]['donamount']),
                                )
    return True






def company_info(request,pid):
    obj = Company.objects.get(id=pid)
    return render(request,'orginfo/company_info.html',locals())

def recur_info(request):
    object_list = Requirement.objects.all()
    return render(request,'orginfo/recruitor.html',locals())





import threading

def printit():
  threading.Timer(5.0, printit).start()
  print "Hello, World!"






from django.views import generic as g
from django.db.models import get_model
from django.http import HttpResponseRedirect


class ManageBase(object):

    @property
    def model(self):
        return get_model('crm', self.kwargs.get('model'))

    def get_form_class(self):

        self.fields = {
            'company': ('name','address','location','type_of_company', ), 'requirement': ('position', 'no_openings','technology','skills','experience','location','type_of_opening','salary_range' )
        }[self.kwargs.get('model')]
        return super(ManageBase, self).get_form_class()


class List(ManageBase, g.ListView):
    template_name = 'orginfo/company_list.html'


class FormBase(ManageBase):

    template_name = 'masterdata/add-edit.html'

    def get_success_url(self):
        return "/masterdata/%s/list/" % (
            self.kwargs.get('model'))


class Create(FormBase, g.CreateView):
    pass


class Update(FormBase, g.UpdateView):
    pass


class Delete(FormBase, g.DeleteView):

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class Status(Delete):

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.switch()
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())









































