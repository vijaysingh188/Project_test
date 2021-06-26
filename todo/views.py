from django.shortcuts import render,redirect
from .models import ToDo,UploadDocuments
from .forms import ToDoForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
def todo_list(request):
    obj = ToDo.objects.all().order_by('-created_at')
    context = {
        'obj':obj
    }
    if request.method == "POST":
        form = ToDoForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect('/todo/api/v1.0/tasks',
                                messages.success(request, 'Task is successfully Created.', 'alert-success'))
            else:
                return redirect('/todo/api/v1.0/tasks', messages.error(request, 'Task is not Valid', 'alert-danger'))
    else:
        form = ToDoForm()
    return render(request,'todo_list.html',context)
@csrf_exempt
def task_edit(request, module_id):
    try:
        module = ToDo.objects.get(id=module_id)
    except:
        return redirect('/todo/api/v1.0/tasks',
                        messages.error(request, 'Task is not found.', 'alert-danger'))


    if request.POST:
        form = ToDoForm(request.POST,instance=module)

        if form.is_valid():
            form.save()
            return redirect('/todo/api/v1.0/tasks', messages.error(request, 'Task successfully updated', 'alert-danger'))

        else:
            return redirect('/todo/api/v1.0/tasks', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        form = ToDoForm(instance=module)

        return render(request, 'task_edit.html', {'form':form})

@csrf_exempt
def task_delete(request, module_id):
    try:
        module = ToDo.objects.get(id=module_id)
    except:
        return redirect('/todo/api/v1.0/tasks',
                        messages.error(request, 'Task is not found.', 'alert-danger'))

    module.delete()
    return redirect('/todo/api/v1.0/tasks', messages.success(request, 'Task is successfully deleted.', 'alert-success'))



def task_status_change(request):
    print("skjbfsjbhsbsvkfsjg")
    status = request.GET
    some_list = ToDo.objects.filter(title=status['id']).values_list('active')
    res = [lis[0] for lis in some_list]

    if res[0] == True:
        some_list =ToDo.objects.filter(title=status['id']).update(active=False)
    elif res[0] == False:
        some_list = ToDo.objects.filter(title=status['id']).update(active=True)
    return HttpResponse()


def uploaddocuments(request):
    print("cfvbkfvf")
    get_all_objects = list(UploadDocuments.objects.values("uploadfiles","filename","created_at"))
    print(get_all_objects,'******************get_all_objects')
    if request.method == "POST":
         print("post")
         myfile = request.FILES['myfile']
         filename = request.POST.get("filename")
         print(myfile,filename)
         object_creation = UploadDocuments.objects.create(uploadfiles=myfile,filename=filename)
         print("successfully")
    context={
        "get_all_objects":get_all_objects
    }
    return render(request,'upload_documents.html',context)

