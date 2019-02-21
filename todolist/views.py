from django.shortcuts import render, redirect
from .models import TODO

# Create your views here.


def home(request):
    if request.method == 'POST':

        content = request.POST.get('待办事项')
        if content:
            a_row = TODO(thing=content, done=False)
            a_row.save()
            content = {'清单': TODO.objects.all(), '信息':'添加成功!'}
            return render(request, 'todolist/home.html', content)
        else:
            return render(request, 'todolist/home.html', {'警告': '请输入内容', '清单':TODO.objects.all()})
    else:
        content = {'清单': TODO.objects.all()}
        return render(request, 'todolist/home.html', content)


def edit(request, thing_id):
    if request.method == 'POST':
        if request.POST.get('已修改事项') == '':
            return render(request, 'todolist/edit.html', {'警告':'请输入内容'})
        else:
            a = TODO.objects.get(id=thing_id)
            a.thing = request.POST['已修改事项']
            a.save()
            return redirect('todolist:主页')
    else:
        content = TODO.objects.get(id=thing_id).thing
        return render(request, 'todolist/edit.html', {'待修改事项':content})

def about(request):
    return render(request, 'todolist/about.html')


def delate(request, thing_id):
    a = TODO.objects.get(id=thing_id)
    a.delete()
    return redirect('todolist:主页')

def cross(request, thing_id):

    if request.POST['完成状态'] == '已完成':
        a = TODO.objects.get(id=thing_id)
        a.done = True
        a.save()
        return redirect('todolist:主页')
    else:
        a = TODO.objects.get(id=thing_id)
        a.done = False
        a.save()
        return redirect('todolist:主页')