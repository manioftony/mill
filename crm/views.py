from __future__ import division
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from crm.models import *
import requests
import json
from django.views import generic as g
from django.db.models import get_model
from django.http import HttpResponseRedirect
from models import Company


# Create your views here.



def log_file(request):
    # import ipdb;ipdb.set_trace()
    # import re
    # obj = open("/var/log/nginx/access.log")
    # obj = obj.readlines()
    # return HttpResponse(obj)
    # import os 
    # mobj=
    # obj1 = os.system("%s"%(obj))
    # obj1 = str(obj1)
    # return HttpResponse(obj1)
    if request.method == 'POST':
        obj = request.POST.get("name")
#        import subprocess,shlex
#        # obj =  subprocess.Popen(shlex.split(str(obj)))
#        # print "----------------------",str(obj)
#        return HttpResponse(subprocess.call("cat  /var/log/nginx/access.log", shell=True))
        import commands
        obj = commands.getstatusoutput(obj)
    return render(request, 'log.html', locals())





def production_list(request):
    if request.method == 'GET':
        obj = Production.objects.all()
        total = sum([i.kg for i in Production.objects.all()])
        loss  = round((7/100)*total)
        yarn = sum([i.yarn_output() for i in Production.objects.all()])

        return render(request, 'masterdata/production_list.html', locals())




def production_data(request):
    if request.method == 'GET':
        return render(request, 'masterdata/production_add.html', locals())
    if request.method == 'POST':
        # import ipdb;ipdb.set_trace()
        kg = request.POST.get('kg')
        date = request.POST.get('date')
        obj = Production.objects.create(kg=kg,date=date)
        return HttpResponseRedirect("/production-list/")








def home(request):
    r1 = requests.get('http://tester.dsdemo.mahiti.org/orginfo-list/')
    r1 = eval(r1.content)
    r2 = requests.get('http://developer.dsdemo.mahiti.org/orginfo-list/')
    r2 = eval(r2.content)
    r3 = requests.get('http://mc.dsdemo.mahiti.org/orginfo-list/')
    r3 = eval(r3.content)
    r4 = requests.get('http://mahiti.dsdemo.mahiti.org/orginfo-list/')
    r4 = eval(r4.content)

    object_list = OrgInfo.objects.filter(active=2)
    return render(request, 'report.html', locals())
  #  return render_to_response("report.html", {"obj_as_json": json.dumps(r1)})


def org_list(request):
    object_list = OrgInfo.objects.filter(active=2)
    return render(request, 'orginfo/list.html', locals())


def sales(request):
    com_obj = Company.objects.all().count()
    sal_obj = Requirement.objects.all().count()
    return render(request, 'orginfo/sales.html', locals())


def company_list(request):
    return render(request, 'orginfo/company_list.html', locals())


def get_current_info():
    return [eval(requests.get('http://%s.dsdemo.mahiti.org/orginfo-list/' % i).content)
            for i in ['mahiti', 'developer', 'tester', 'mc']]


def update_org_info():
    OrgInfo.objects.all().delete()
    org_info = get_current_info()
    for i in range(len(org_info)):
        OrgInfo.objects.create(customer_name=org_info[i]['orgname'],
                               no_of_profile=org_info[i]['proinfo'],
                               no_of_donation=org_info[i]['doninfo'],
                               total_amount=float(org_info[i]['donamount']),
                               )
    return True


def company_info(request, pid):
    obj = Company.objects.get(id=pid)
    return render(request, 'orginfo/company_info.html', locals())


def recur_info(request):
    object_list = Requirement.objects.all()
    return render(request, 'orginfo/recruitor.html', locals())





def recur_info_data(request, pid, model):
    # import ipdb;ipdb.set_trace()
    obj = Requirement.objects.get(id=pid)
    obj.current_status = {'open': 1, 'inprogress': 2}.get(model)
    obj.save()
    return HttpResponseRedirect("/recur_info/")


def resume_save(request, pid):

    if request.method == 'GET':
        obj = Requirement.objects.get(id=pid)
        return render(request, 'orginfo/resume.html', locals())
    if request.method == 'POST':
        obj = Requirement.objects.get(id=pid)
        obj.current_status = 2
        obj.resume = request.FILES['image_file']
        obj.save()
        return HttpResponseRedirect("/recur_info/")


import threading


def printit():
    threading.Timer(5.0, printit).start()
    print "Hello, World!"


class ManageBase(object):

    @property
    def model(self):
        return get_model('crm', self.kwargs.get('model'))

    def get_form_class(self):

        self.fields = {
            'company': ('name', 'address', 'location', 'type_of_company', ),
            'requirement': ('position', 'no_openings', 'technology', 'skills', 'experience', 'location', 'type_of_opening', 'salary_range'),
            'profile': ('first_name','last_name','gender','blood_group','current_address','permanet_address','joining_date','date_of_birth','mobile_number','landline_number','voter_id','driving_license','aadhar_card',),
            'employeeinfo': ('employee_id','working_shift','login_time','logout_time','employee_role','under_supervision','break_time','over_time',)
        }[self.kwargs.get('model')]
        return super(ManageBase, self).get_form_class()

    # def get_queryset(self, *args, **kwargs):

    #     modl = self.kwargs['model']

    #     if modl == 'requirement':
    #         return Requirement.objects.filter(company_id=self.kwargs['pk'])
    #     if modl == 'company':
    #         return Company.objects.all()

    # def form_valid(self, form):
    #     if self.kwargs['model'] == 'requirement':
    #         self.object = form.save()
    #         self.object.company = Company.objects.get(id=self.kwargs['pk'])
    #         self.object.unique_id = str('%s%s000%s' % (self.object.company.name[
    #                                     :3], self.object.position[:3], self.object.company.id))
    #         self.object.save()
    #         return HttpResponseRedirect('/masterdata/requirement/list/%s' % (self.kwargs['pk']))
    #     self.object = form.save()
    #     return HttpResponseRedirect(self.get_success_url())


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
