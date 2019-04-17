import datetime

from django.shortcuts import render, redirect

from todolist.models import TodoList



def index(request):
    todo = TodoList.objects.all()

    if request.method == "POST":
        print(request.POST, "hi")

        if "taskAdd" in request.POST:
            author = request.POST['author']
            if author == '':
                author = 'anonymous'

            title = request.POST["title"]
            description = request.POST["description"]
            created = str(datetime.date.today())

            due_date = str(request.POST["duedate"])
            datetime_object = datetime.datetime.strptime(due_date, "%Y-%m-%d").date()
            print(datetime_object, 'checkdatetime')
            if due_date <= created:
                print(datetime.date.today()+datetime.timedelta(days=1))
                due_date = str(datetime.date.today()+datetime.timedelta(days=1))
            else:
                due_date = due_date


            todo = TodoList(author = author, title = title, created = created,due_date = due_date, description = description)
            todo.save()
            return redirect("/todo/")

    #     print("testing")
    #     if "delete" in request.POST:
    #         print("testing")
    #         print("testing1",request.POST.get('delete'))
    #         checkedlist =  request.POST.get('delete')
    #         todo = TodoList.objects.get(id=int(checkedlist))
    #         todo.delete()
    #
    return render(request, "index.html", {"todos": todo})





