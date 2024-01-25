from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Task
from .forms import Todoform
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView


# classbased generic views

class Tasklistview(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task1'

class Taskdetailview(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task2'

class TaskUpdateview(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','Date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})


class TaskDeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')



# Create your views here.


def add(request):
    task1 = Task.objects.all()
    if request.method == 'POST':
        name=request.POST.get('task')
        priority=request.POST.get('priority')
        date=request.POST.get('Date')
        task=Task(name=name,priority=priority,Date=date)
        task.save()



    return render(request,'home.html',{'task1':task1})


def delete(request,id):
    tsk=Task.objects.get(id=id)
    if request.method=='POST':
        tsk.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    task=Task.objects.get(id=id)
    f=Todoform(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')

    return render(request,'edit.html',{'f':f})


# def detail(request):
#
#     return render(request,'detail.html',)
