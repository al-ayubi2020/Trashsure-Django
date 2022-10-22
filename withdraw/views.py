from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from rolepermissions.decorators import has_role_decorator
from project_django.roles import commonUser
from rolepermissions.roles import assign_role, get_user_roles
from rolepermissions.checkers import has_role
from django.http.response import JsonResponse
from django.core import serializers
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from admin_page.models import Withdraw
from landing_page.models import UserData



@login_required(login_url='/login/')
def index(request):
    user = request.user
    role = get_user_roles(user)
    if (has_role(user, commonUser)):
        return render(request, 'index_withdraw.html')
    return redirect('/login/')

@login_required(login_url='/login/')
def add(request):
    user = request.user
    role = get_user_roles(user)
    if has_role(user, commonUser):
        if request.method == 'POST':
            jumlah = int(request.POST.get('jumlah'))
            userdata = UserData.objects.get(user=user)
            if (userdata.balance >= jumlah):
                withdraw = Withdraw(jumlah=jumlah, user=user)
                withdraw.save()
                userdata.balance -= jumlah
                userdata.save()
                return JsonResponse({"instance": "Penarikan Berhasil"}, status=200) 
            return JsonResponse({"instance": "Saldo Kurang"}, status=200) 
        return redirect('withdraw:index')
    return redirect('/login/')

@login_required(login_url='/login/')
def get(request):
    user = request.user
    role = get_user_roles(user)
    if (has_role(user, commonUser)):
        withdraw = Withdraw.objects.filter(user=user).order_by('-pk')
        return HttpResponse(serializers.serialize("json", withdraw), content_type="application/json")
    return redirect('/login/')