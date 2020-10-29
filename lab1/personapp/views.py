from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view, renderer_classes
from django.http import JsonResponse
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
# Create your views here.
from .models import Person
from .serializers import PersonSerializer
from rest_framework import status

class Persons(APIView):

    def get(self, request, pk=None, format=None):
        if not pk:
            persons = Person.objects.all()
            serializer = PersonSerializer(persons, many=True)
            return Response(serializer.data)
        person = get_object_or_404(Person, pk=pk)
        serializer = PersonSerializer(instance=person)

        return Response(serializer.data)

    def post(self, request, format=None):

        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            saved_data = serializer.save()
        return Response(None, status=status.HTTP_201_CREATED, headers={"location":"https://rsoi-personservice.herokuapp.com/person/{}".format(saved_data.id)})

    def patch(self, request, pk):
        existed_person = get_object_or_404(Person, pk=pk)
        data = request.data
        serializer = PersonSerializer(instance=existed_person, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            saved_person = serializer.save()
        return Response({"id": "{}".format(saved_person.id)}) # {"success": " updated successfully  '{}'".format(saved_person.id)})

    def delete(self, request, pk):
        existed_person = get_object_or_404(Person, pk=pk)
        if existed_person:
            existed_person.delete()
        return Response(status=204)

