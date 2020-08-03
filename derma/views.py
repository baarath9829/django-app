from django.shortcuts import render
from django.http import HttpResponse
from fastai.vision import *
from fastai.metrics import error_rate
from pathlib import Path
from .models import input
# Create your views here.
def index(request):
    return render(request,'derma/index.html')

def core(request):
    name = "Nothing"
    static_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'static')
    print(static_path)
    if request.method == 'POST':
        for i in request.FILES:
            print(i);
            #print(".");
        file = request.FILES['inputfile']
        obj = input(label="mela",image=file)
        obj.save()
        #print(file);
        if(file.content_type=='image/jpeg'):
            with open(static_path+'/derma/image/test-img.jpeg', 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            learn = load_learner(static_path+'/derma/asserts', 'trained_model101.pkl')
            img_path = os.path.join(static_path,"derma/image/test-img.jpeg")
            img = open_image(img_path)
            predict = learn.predict(img)
            name = str(predict[0])
            prob = round((max(predict[2])*100).item(),2)
        else:
            print(file.content_type)
            return render(request,'derma/index.html')
    context={'result':name, 'prob':prob}
    return render(request,'derma/result.html',context)