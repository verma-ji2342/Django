"""
View.py
"""

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from home.models import Person
from home.serializer import PeopleSerializer


class PersonViewSet(viewsets.ModelViewSet):
    """
    PersonViewSet class
    """
    queryset = Person.objects.all()
    serializer_class = PeopleSerializer


@api_view(['GET', 'POST'])
def index(request):
    """
    index function
    """
    print(request.method)
    courses = {
        'course_name': "python django",
        "tutor" : "Pranjal",
        "validity": "3 months",
    }

    return Response(courses)

@api_view(['GET', 'POST'])
def person(request):
    """
    person function
    """

    if request.method == 'GET':
        objs = Person.objects.all()
        print(objs)
        serializer = PeopleSerializer(objs, many = True)
        return  Response(serializer.data)
    
    else:
        data = request.data
        print(data)
        serializer = PeopleSerializer(data = data)
        print(serializer)
        print("*********************")
        if serializer.is_valid():
            print("yes...")
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
