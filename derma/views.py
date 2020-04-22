from django.shortcuts import render
from django.http import HttpResponse
from fastai.vision import *
from fastai.metrics import error_rate
from pathlib import Path


# Create your views here.
def index(request):
    return render(request,'derma/index.html')

def core(request):
    predict_name= "Nothing"
    if request.method == 'POST':
        for i in request.FILES:
            print(i);
            print(".");
        file = request.FILES['inputfile']
        #print(file);
        if(file.content_type=='image/jpeg'):
            with open('derma/static/image/test-img.jpeg', 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            learn = load_learner('derma/static/asserts', 'trained_model101.pkl')
            img_path = Path('derma/static/image/test-img.jpeg')
            img = open_image(img_path)
            predict_name = str(learn.predict(img)[0])
        else:
            print(file.content_type)
            return render(request,'derma/index.html')
    context={'result':predict_name}
    return render(request,'derma/result.html',context)