from django.shortcuts import HttpResponse, redirect, get_object_or_404, render
from .models import Task  # adjust import if your model is named differently

def todos(request):
    # tasks = Task.objects.filter(is_completed=False)
    tasks = Task.objects.all()
    context ={"todos": tasks}
    return render(request, "todo.html", context)

def todo_details(request, pk):
    task = get_object_or_404(Task, pk=pk)
    context ={"task": task}
    return render(request, "todo_detail.html", context)

def addTodo(request):
    if request.method == "POST":
        task = request.POST.get("task")
        description = request.POST.get("description", "")
        is_completed = bool(request.POST.get("is_completed"))

        if task:  # basic validation
            Task.objects.create(
                task=task,
                description=description,
                is_completed=is_completed,
            )
    return redirect("todos")