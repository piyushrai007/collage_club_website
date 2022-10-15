from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    context = {
        "variable":"this is sent",
        "variable2": "piyush"

    }
    return render(request, 'index.html',context)
    # return HttpResponse("this is PIYUSH RAI")

def about(request):
    return render(request, 'about.html',)
    # return HttpResponse("this is about")

def services(request):
    return HttpResponse("this is services ")
    
def contact(request):
    return render(request, 'contact.html',)
    # return HttpResponse("this is contact ")            
