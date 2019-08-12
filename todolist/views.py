import datetime
import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from todolist.models import TodoList


def index(request):
    print(request.POST, 'r')
    todos = TodoList.objects.all().order_by('-id')

    if request.method == "POST":

        updatelistid = 0
        bool = False
        data0 = ''
        data1 = ''
        data2 = ''
        data3 = ''
        data4 = ''
        data5 = ''

        if "id" in request.POST:
            updatelistid = request.POST["id"]
            print(updatelistid, 'update id finding')

        if "author" in request.POST:
            response_data = {}

            author = request.POST['author']
            title = request.POST["title"]
            description = request.POST["description"]
            due_date = str(request.POST["duedate"])

            if author == '':
                author = 'anonymous'

            now = datetime.datetime.utcnow()
            rounded = now - datetime.timedelta(minutes=now.minute%5 +5)
            # t = datetime.timedelta(minutes=now.minute-5)
            # print(t, 'tttt')
            print(rounded, 'roooouuuu')

            author_create = TodoList.objects.filter(author=author)

            if author_create.exists() and author != 'anonymous':
                a = author_create.order_by('-id')[0]
                author_create_time = a.created
                author_create_time = author_create_time.replace(tzinfo=None)
                if author_create_time > rounded:
                    bool = True
                    data0 = {'status': 'false', 'message_0': 'please enter after 3 minutes'}

            title_temp = title.lower()
            title_temp2 = title.upper()
            title_list = TodoList.objects.filter(title=title_temp)
            title_list1 = TodoList.objects.filter(title=title_temp2)
            if title == '':
                bool = True
                data1 = {'status': 'false', 'message_2': 'Enter the Title pls'}
            elif title_list.exists() or title_list1.exists():
                bool = True
                data1 = {'status': 'false', 'message_2': 'title already exsist'}

            if description == '':
                bool = True
                data2 = {'status': 'false', 'message_1': 'description not found'}
            else:
                if len(description) >= 10:
                    bool = True
                    data2 = {'status': 'false', 'message_1': 'description not more than 10 characters'}

            if due_date == '':
                bool = True
                data3 = {'status': 'false', 'message':'due date pls'}
            else:
                date_object = datetime.datetime.strptime(due_date, "%Y-%m-%d").date()
                if date_object <= datetime.date.today():
                    bool = True
                    data3 = {'status': 'false', 'message': 'valid due date pls'}

            data = {'data1': data1, 'data2': data2, 'data3': data3, 'data4':data4, 'data5':data5, 'data0':data0}
            print(data)

            if bool == True:
                return JsonResponse(data, status=400)

            elif TodoList.objects.filter(id=updatelistid).exists():
                todo = TodoList.objects.filter(id=request.POST["id"]).update(author=author,
                                                                       title=title, due_date=due_date,
                                                                       description=description)
            else:
                todo = TodoList(author=author, title=title, due_date=due_date, description=description)
                todo.save()
                response_data['id'] = todo.id
                response_data['author'] = todo.author
                response_data['title'] = todo.title
                response_data['description'] = todo.description
                response_data['due_date'] = todo.due_date

                return HttpResponse(json.dumps(response_data),
                                    content_type="application/json")

    if request.method == 'POST':

        if "delete" in request.POST:
            print(request.POST, "checking post")
            checkedlist = request.POST["delete"]
            print(checkedlist, "chekkk list")
            try:
                todo = TodoList.objects.get(id=checkedlist)
                print(todo, 'viewsdele')
                todo.delete()
            except todo.DoesNotExist:
                return "id does not exist"

    return render(request, "index.html", {"todos": todos})







