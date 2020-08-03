from django.shortcuts import render,HttpResponse,redirect
from .models import Tasks
# Create your views here.
# def index(request):
#     tasks=Tasks.objects.all()
#     return render(request,'todoapp/index.html',{'tasks':tasks})
# def add_form(request):
#     if request.method=="POST":
#         name=request.POST.get("name","")
#         priority=request.POST.get("priority","")
#         task=Tasks(name=name,priority=priority)
#         task.save()
#         return redirect('/')
#     return render(request,'todoapp/add.html')
def index_form(request):
    if request.method=="POST":
        name=request.POST.get("name","")
        priority=request.POST.get("priority","")
        task=Tasks(name=name,priority=priority)
        task.save()
        return redirect('/')
    else:
        tasks=Tasks.objects.all()
        return render(request,'todoapp/index.html',{'tasks':tasks})
def delete(request,id):
    task=Tasks.objects.get(id=id)
    if request.method=="POST":
        task.delete()
        return redirect('/')
    return render(request,'todoapp/delete.html')