from django.shortcuts import render
from rest_framework import generics
from .models import Peanut
from .serializers import PeanutSerializer
from .permissions import IsAuthorOrReadOnly

# Create your views here.
class PeanutList(generics.ListCreateAPIView):
    queryset = Peanut.objects.all()
    serializer_class = PeanutSerializer


class PeanutDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Peanut.objects.all()
    serializer_class = PeanutSerializer
    permission_classes = (IsAuthorOrReadOnly,)
    print(permission_classes)