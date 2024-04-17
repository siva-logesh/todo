from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import todolist
def home(request):
    return render(request,'home.html')
def start_up(request):
    all_todolist=todolist.objects.all()
    return render(request,'todo.html',{'full_list':all_todolist})
def addtask(request):
    new_task=todolist(tasks=request.POST['content'])
    new_task.save()
    return HttpResponseRedirect('/todo/')
def done(request,task_id):
    taskdone=todolist.objects.get(id=task_id)
    taskdone.delete()
    return HttpResponseRedirect('/todo/')

# Create your views here.
