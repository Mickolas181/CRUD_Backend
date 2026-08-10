from rest_framework.response import Response
from .models import task
from rest_framework.decorators import api_view
from django.shortcuts import render
from .serializers import taskserializer


@api_view(['GET'])
def Task_list(request):
    Task = task.objects.all()
    serializer = taskserializer(Task, many=True)
    return Response( serializer.data)


@api_view(['POST'])
def Task_create(request):
    serializer = taskserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def Task_delete(request, pk):
    try:
        Task = task.objects.get(id=pk)
        Task.delete()
        return Response("Task Deleted")
    except task.DoesNotExist:
        return Response("Task not found", status=404)


@api_view(['PUT'])
def Task_update(request, pk):
    try:
        Task = task.objects.get(id=pk)
        serializer = taskserializer(instance=Task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    except task.DoesNotExist:
        return Response("Task not found", status=404)



    