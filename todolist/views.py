import datetime
from django.shortcuts import render, redirect
from todolist.models import TodoList

def index(request):
    todo = TodoList.objects.all()

    if request.method == "POST":
        if "taskAdd" in request.POST:
            author = request.POST['author']
            if author == '':
                author = 'anonymous'
            title = request.POST["title"]
            description = request.POST["description"]
            created = str(datetime.date.today())
            due_date = str(request.POST["duedate"])
            datetime_object = datetime.datetime.strptime(due_date, "%Y-%m-%d").date()
            if datetime_object <= datetime.date.today():
                due_date = str(datetime.date.today() + datetime.timedelta(days=1))
            due_date = due_date
            todo = TodoList(author = author, title = title, created = created,due_date = due_date, description = description)
            todo.save()
            return redirect("/todo/")

        if "delete" in request.POST:
            checkedlist = request.POST["delete"]
            try:
                todo = TodoList.objects.filter(id=checkedlist)
                todo.delete()
            except todo.DoesNotExist:
                return "id does not exist"

    return render(request, "index.html", {"todos": todo})






