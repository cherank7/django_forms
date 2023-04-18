from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def student(request):
    sfo=Student()
    d={'sfo':sfo}
    if request.method=='POST':
        f=Student(request.POST)
        if f.is_valid():
            return HttpResponse(str(f.cleaned_data))

    return render(request,'student.html',context=d)
