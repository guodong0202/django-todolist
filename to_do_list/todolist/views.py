from django.shortcuts import render, redirect

# Create your views here.

lst = [
    {'base_tasks': 'play with dog', 'Status': False},
    {'base_tasks': 'play with wife', 'Status': True},
]

def home(request):
    global lst
    if request.method == "POST":
        if request.POST['base_tasks'] == '':
            content = {'tasklist': lst, "Alert": "请输入内容！"}
            return render(request, "todolist/home.html", content)
        else:
            lst.append({'base_tasks': request.POST['base_tasks'], 'Status': False})
            content = {'tasklist': lst, "Info": "添加成功！"}
            return render(request, "todolist/home.html", content)
    elif request.method == "GET":
        content = {'tasklist': lst}
        return render(request, "todolist/home.html", content)


# 默认会到所有templates文件夹中去寻找指定的html

def about(request):
    return render(request, "todolist/about.html")


def edit(request, forloop_counter):
    global lst
    if request.method == "POST":
        if request.POST['editedlist'] == '':
            return render(request, "todolist/edit.html", {"Alert": "请输入内容！"})
        else:
            lst[int(forloop_counter) - 1]['base_tasks'] = request.POST['editedlist']
            return redirect("todolist:home")
    elif request.method == "GET":
        content = {'editlist': lst[int(forloop_counter) - 1]['base_tasks']}
        return render(request, "todolist/edit.html", content)


def delete(request, forloop_counter):
    lst.pop(int(forloop_counter) - 1)
    return redirect("todolist:home")


# def cancle(request, forloop_counter):
#     global lst
#     return redirect("todolist:home")


def strike(request, forloop_counter):
    global lst
    if request.POST['str_status'] == 'completed':
        lst[int(forloop_counter) - 1]['Status'] = True
    else:
        lst[int(forloop_counter) - 1]['Status'] = False
    return redirect("todolist:home")
