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





import threading

def printit():
  threading.Timer(5.0, printit).start()
  print "Hello, World!"











