from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
  return render(request,'home.html', {'name':'Wellcome to cancer predictions','link':'https://github.com/atulcoin'})
def add(request):
  val1 = int(request.POST['num1'])
  val2 = int(request.POST['num2'])

  res = val1 + val2
  res1 = val1 * val2
  res2 = 9.8+val1*val2

  return render(request,'result.html', {'result':res,'result3':res2, 'resul2':res1,'link':'http://127.0.0.1:8000'})