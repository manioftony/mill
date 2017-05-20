from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,logout
from django.views.decorators.csrf import csrf_exempt
from crm.forms import *








def user_login(request):
#    import ipdb;ipdb.set_trace()
    if request.user.is_authenticated():
        return HttpResponseRedirect('/sales-list/')
    form = LoginForm()
    if request.method != 'POST':
        return render(request, 'login.html', locals())

    form = LoginForm(request.POST)
    if form.is_valid():
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user is not None :
            if user.is_active:
                login(request, user)
                # return HttpResponseRedirect('/sales-list/')
                return HttpResponse('hi')
            else:
                message = "User is not active"
        else:
            message = "Invalid Username or Password"
        
    return render(request, 'login.html', locals())































@csrf_exempt
def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/")

