from django.shortcuts import render
from django.http import HttpResponse
# Create your views here. 
import pandas as pd
from sklearn.externals import joblib
reloadmodel = joblib.load('./models/titanicmodel.pkl')

def home(request):
  return render(request,'home.html', {'name':'Wellcome to cancer predictions','link':'https://github.com/atulcoin'})

def add(request):
  val1 = int(request.POST['num1'])
  val2 = int(request.POST['num2'])
  val3 = int(request.POST['num3'])

  res = 'res teriwatt lagg gyi'
  res2 = 'res1 ghar me reh'
  
  new_data ={'Pclass': [val1], 'Age':[val2], 'Sex':[val3]}
  nwdf=pd.DataFrame(new_data, columns =['Pclass','Age', 'Sex'])
  print(nwdf)
  if reloadmodel.predict(nwdf) == 0:
       return render(request,'result.html', {'result':res,'link':'http://127.0.0.1:8000'})
  if reloadmodel.predict(nwdf) == 1:
       return render(request,'result2.html', {'result3':res2,'link':'http://127.0.0.1:8000'})

def updatedata(request):
    return None