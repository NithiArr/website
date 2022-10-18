from django.shortcuts import render
from base.models import crudst
from django.db.models import Q


def home(request):
    return render(request, 'home.html')
def totalorder(request):
    results=crudst.objects.all()
    return render(request,"totalorder.html",{"crudst":results})

def orderdelivered(request):
        status = 'delivered'
        emps = crudst.objects.all()
        if status:
            emps = emps.filter(Q(status__icontains = status))
        return render(request, 'orderdeliver.html', {'detail': emps})

def pending(request):
        status = 'pending'
        emps = crudst.objects.all()
        if status:
            emps = emps.filter(Q(status__icontains = status))
        return render(request, 'orderdeliver.html', {'detail': emps})