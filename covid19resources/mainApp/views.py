from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import CovidResource


# Create your views here.
def index(request):
    context=dict()
    if request.method=='POST':
        search_tag=request.POST['s_tag']
        s_resources=CovidResource.objects.filter(tags__contains=search_tag)
        context={'resources':s_resources}
    else:
        resources=CovidResource.objects.order_by('-date_added')
        context={'resources':resources}
    return render(request,'mainApp/index.html',context)


def add_new(request):
    if request.method=='POST':
        resource_type=request.POST['resourceType'].strip()
        state=request.POST['state'].strip()
        city=request.POST['city'].strip()
        title=request.POST['title'].strip()
        description=request.POST['description'].strip()
        tags=request.POST['tags'].strip()
        try:
            image1=request.FILES['image1']
        except:
            image1=None
        try:
            image2=request.FILES['image2']
        except:
            image2=None
        try:
            image3=request.FILES['image3']
        except:
            image3=None
        obj=CovidResource(resource_type=resource_type,state=state,city=city,title=title,description=description,tags=tags,image1=image1,image2=image2,image3=image3)
        obj.save()
        response={"status_code":"OK"}
        return JsonResponse(response)
        
    return render(request,'mainApp/addnew.html')


def filter_search(request):
    if request.method=='POST':
        resource_type=request.POST['resourceType'].strip()
        state=request.POST['state'].strip()
        city=request.POST['city'].strip()
        print(resource_type,state,city)
        obj=CovidResource.objects.filter(resource_type=resource_type).filter(state=state).filter(city=city)
        context={'resources':obj,'s_resource':resource_type,'s_state':state,'s_city':city}
        return render(request,'mainApp/index.html',context)
