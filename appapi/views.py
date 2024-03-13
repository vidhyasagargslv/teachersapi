from django.shortcuts import render
from rest_framework import viewsets
from appapi.models import TeachersModel
from appapi.serializers import TeachersSerializer
from rest_framework.permissions import IsAdminUser


# Create your views here.
#todo we dont use function here , we use rest_frameowrk here for functions

class TeachersViewSet(viewsets.ModelViewSet):
    queryset = TeachersModel.objects.all()
    serializer_class = TeachersSerializer
    


#? The ModelViewSet class provides the basic actions for a model, such as list, create, retrieve, update, and destroy.
#? The ModelViewSet class is appropriate when you need to provide a full CRUD interface for a model.
#? We are using the ModelViewSet class to create a viewset for our StudentModel model.
#? The queryset attribute is used to specify the queryset that will be used to retrieve the objects that will be displayed in the API.
#? In this case, we are using the StudentModel.objects.all() method to retrieve all the objects in the StudentModel model.
    