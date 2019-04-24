import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework.exceptions import ValidationError

from todolist.models import TodoList


def index(request):
    todos = TodoList.objects.all()

    if request.method == "POST":
        if "taskAdd" in request.POST:
            author = request.POST['author']
            if author == '':
                author = 'anonymous'
            title = request.POST["title"]
            description = request.POST["description"]
            due_date = str(request.POST["duedate"])

            if due_date == '':
                return HttpResponse("please enter a date")

            datetime_object = datetime.datetime.strptime(due_date, "%Y-%m-%d").date()
            if datetime_object <= datetime.date.today():
                return HttpResponse("plaese enter a correct date")


                # due_date = str(datetime.date.today() + datetime.timedelta(days=1))
            due_date = due_date
            todo = TodoList(author = author, title = title, due_date = due_date, description = description)
            todo.save()
            return redirect("/todo/")

        if "delete" in request.POST:
            checkedlist = request.POST["delete"]
            try:
                todo = TodoList.objects.filter(id=checkedlist)
                todo.delete()
            except todo.DoesNotExist:
                return "id does not exist"

    return render(request, "index.html", {"todos": todos})






