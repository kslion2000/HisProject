from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import HttpResponse
from django.contrib import messages
from .forms import *
from users.models import New_user
from django.conf import settings
import requests
import json

def register(request):
    if request.method == 'POST':
        form = New_userForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in.')
            return redirect('login')
    else:
        form = New_userForm()
    return render(request, 'users/register.html', {'form': form})

@login_required()
def appointment(request):
    user_id = request.user.id
    user_info = New_user.objects.get(user_ptr_id=user_id)
    user_form = New_userForm(instance=user_info)
    site_key = settings.RECAPTCHA_SITE_KEY
    if request.method == 'POST':
        datas = request.POST
        form = AppointmentIssueForm(datas)
        print(form)
        if form.is_valid():
            form.save()
        print(aaa)
        recaptcha_response = datas.getlist('g-recaptcha-response')[0]
        data = {
            'secret': settings.RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()

        if result['success']:
            result = {'result': True, 'message': 'Save success.'}
            return HttpResponse(json.dumps(result), content_type='application/json')
        else:
            result = {'result': False, 'message': 'Fail!'}
            return HttpResponse(json.dumps(result), content_type='application/json')
    else:
        return render(request, 'users/appointment.html', locals())