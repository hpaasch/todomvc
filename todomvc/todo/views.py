from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics

import json

from todo.models import Todo
from todo.serializers import TodoSerializer


class TodoListAPIView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
