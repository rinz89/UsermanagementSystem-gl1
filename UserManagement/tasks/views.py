from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from rest_framework.parsers import JSONParser
from .models import Task
from .serializers import *


def wants_json(request):
    return request.headers.get('Content-Type') == 'application/json' or request.headers.get('Accept') == 'application/json'



@csrf_exempt
@login_required
def create_task(request):
    if request.method == 'POST':
        if wants_json(request):
            data = JSONParser().parse(request)
            serializer = TaskSerializer(data=data)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return JsonResponse({'message': 'Task created successfully', 'task': serializer.data}, status=201)
            return JsonResponse(serializer.errors, status=400)
        else:
            Task.objects.create(
                user=request.user,
                title=request.POST.get('title'),
                description=request.POST.get('description'),
                attachment=request.FILES.get('attachment')
            )
            return redirect('listtask')

    return render(request, 'tasks/create.html')



@login_required
def list_tasks(request):
    tasks = Task.objects.filter(user=request.user)

    if wants_json(request):
        serializer = TaskSerializer(tasks, many=True)
        return JsonResponse({'tasks': serializer.data}, status=200, safe=False)

    return render(request, 'tasks/tasklist.html', {'tasks': tasks})



@csrf_exempt
@login_required
def update_task(request, id):
    try:
        task = Task.objects.get(id=id, user=request.user)
    except Task.DoesNotExist:
        return JsonResponse({'error': 'Task not found'}, status=404) if wants_json(request) else redirect('listtask')

    if request.method == 'POST':
        if wants_json(request):
            data = JSONParser().parse(request)
            serializer = TaskSerializer(task, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'message': 'Task updated successfully', 'task': serializer.data}, status=200)
            return JsonResponse(serializer.errors, status=400)
        else:
            task.title = request.POST.get('title', task.title)
            task.description = request.POST.get('description', task.description)
            if 'attachment' in request.FILES:
                task.attachment = request.FILES['attachment']
            task.save()
            return redirect('listtask')

    return render(request, 'tasks/updatetask.html', {'task': task})



@csrf_exempt
@login_required
def delete_task(request, id):
    try:
        task = Task.objects.get(id=id, user=request.user)
    except Task.DoesNotExist:
        return JsonResponse({'error': 'Task not found'}, status=404) if wants_json(request) else redirect('listtask')

    task.delete()

    if wants_json(request):
        return JsonResponse({'message': 'Task deleted successfully'}, status=200)
    else:
        return redirect('listtask')








