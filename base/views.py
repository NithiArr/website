from inspect import modulesbyfile
from django.shortcuts import render
from base.models import crudst
from django.contrib import messages
from base.forms import stform
from .filters import  crudstFilter
from django.db.models import Q

def homee(request):
    results=crudst.objects.all()
    return render(request,"home.html",{"crudst":results})

def stdisplay(request):
    results=crudst.objects.all()
    return render(request,"base.html",{"crudst":results})

def stinsert(request):
    if request.method == "POST":
        if request.POST.get('stname') and request.POST.get('stemail') and request.POST.get('staddress') and request.POST.get('sno'):
            savest = crudst()
            savest.stname=request.POST.get('stname')
            savest.stemail=request.POST.get('stemail')
            savest.staddress=request.POST.get('staddress')
            savest.sno=request.POST.get('sno')
            savest.save()
            messages.success(request,"the record"+savest.stname+"is saved successfully..!")
            return render(request,"base.html") 
    else:
        return render(request,"base.html")

def stedit(request,id):
    getstudentdetails = crudst.objects.get(id=id)
    return render(request,"edit.html",{"crudst":getstudentdetails})

def stupdate(request,id):
    stupdate=crudst.objects.get(id=id)
    form = stform(request.POST,instance=stupdate)
    if form.is_valid():
        form.save()
        messages.success(request,"the student record hasbeen updated successfully!!")
        return render(request,"edit.html",{"crudst":stupdate})
def stdel(request,id):
    delstudent = crudst.objects.get(id=id)
    delstudent.delete()
    results=crudst.objects.all()
    return render(request,"base.html",{"crudst":results})



def searchpage(request):
    if request.method == 'POST':
        no = request.POST['sno']
        emps = crudst.objects.all()
        if no:
            emps = emps.filter(Q(sno__icontains = no))
<<<<<<< HEAD
        return render(request, 'base.html', {'detail': emps})
    else:
        str='Pls enter valid ID'
        return render(request,'base.html',{'cont':str})
=======
        return render(request, 'search.html', {'detail': emps})
    else:
        str='Pls enter valid ID'
        return render(request,'search.html',{'cont':str})
>>>>>>> ce7b21d17771f981ed22fc15ad7ac7aef526c1dd
