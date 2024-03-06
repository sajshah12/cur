from django.shortcuts import render, HttpResponseRedirect
from.models import Info
from.form import InfoForm
# Create your views here.



def add (request):
    yu=Info.objects.all()
    if request.method=='POST':
        yum=InfoForm(request.POST)
        if yum.is_valid():
            yum.save()
            yum=InfoForm()
    else:
        yum=InfoForm()
    return render(request , 'add.html',{'form':yum,'yu':yu})



# delete student information

def delete(request, id):
    if request.method=='POST':
        num = Info.objects.get(pk=id)
        num.delete()
    return  HttpResponseRedirect('/')



#  update student informatio


def update(request,id):
    if request.method == 'POST':
        sm = Info.objects.get(pk=id)
        ym =InfoForm(request.post,isinstance=sm)
        if ym.is_valid():
            ym.save()
            ym = InfoForm()

        else:
            sm = Info.objects.get(pk=id)
            ym = InfoForm(instance=sm)
    return render(request,'update.html',{'form':ym})



