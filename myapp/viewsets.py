from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import django_data
from .serializers import MyModelSerializer

class MyModelViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = django_data.objects.all()
        serializer = MyModelSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = MyModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = django_data.objects.all()
        instance = get_object_or_404(queryset, pk=pk)
        serializer = MyModelSerializer(instance)
        return Response(serializer.data)

    def update(self, request, pk=None):
        instance = django_data.objects.get(pk=pk)
        serializer = MyModelSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        instance = django_data.objects.get(pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
