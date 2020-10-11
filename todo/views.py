from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.views import View
from .models import Todo
from .forms import TodoForm
import datetime

class IndexView(TemplateView):
    template_name = 'todo/index.html'

    def get(self,request):
        form = TodoForm()

        todo_list = Todo.objects.order_by('id')
        mydate = datetime.datetime.now()
        args = {
            'todo_list':todo_list,
            'form':form,
            'mydate':mydate
        }
        return render(request, self.template_name, args)

    def post(self,request):
        form = TodoForm(request.POST)
        if form.is_valid():
            text = form.save()
            text.save()
            return redirect('index')

        args = {'form':form, 'text':text}
        return render(request,self.template_name, args)

class CompleteTodo(View):
    #template_name = 'todo/index.html'

    def get(self,request,todo_id):
        todo = Todo.objects.get(pk = todo_id)
        todo.complete = True
        todo.save()
        return redirect('index')

class DeleteCompleted(View):

    def get(self,request):
        Todo.objects.filter(complete__exact = True).delete()

        return redirect('index')

class DeleteAllTodo(View):

    def get(self,request):
        Todo.objects.all().delete()

        return redirect('index')

class delete_todo(View):
    def get(self,request,id):
        obj = Todo.objects.get(id=id)
        obj.delete()
        return redirect('index')
 