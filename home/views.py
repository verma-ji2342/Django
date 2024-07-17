"""
View.py
"""

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from home.models import Person
from home.serializer import PeopleSerializer, LoginSerializer
from rest_framework.views import APIView

class PersonViewSet(viewsets.ModelViewSet):
    """
    PersonViewSet class
    """

    queryset = Person.objects.all()
    serializer_class = PeopleSerializer


@api_view(["GET", "POST"])
def index(request):
    """
    index function
    """
    print(request.method)
    courses = {
        "course_name": "python django",
        "tutor": "Pranjal",
        "validity": "3 months",
    }

    return Response(courses)


@api_view(["GET", "POST"])
def person(request):
    """
    person function
    """

    if request.method == "GET":
        objs = Person.objects.all()
        print(objs)
        serializer = PeopleSerializer(objs, many=True)
        return Response(serializer.data)

    else:
        data = request.data
        print(data)
        serializer = PeopleSerializer(data=data)
        print(serializer)
        print("*********************")
        if serializer.is_valid():
            print("yes...")
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


@api_view(["GET", "POST", "PUT", "PATCH"])
def edit_person(request):
    """
    PUT function
    """
    print("----------------------------------------")
    if request.method == "PUT":
        data = request.data
        serializer = PeopleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    if request.method == "PATCH":
        data = request.data
        obj = Person.objects.get(id = data['id'])
        serializer = PeopleSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response({"message": "Hit a PUT request"})


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def delete_data(request):
    
    if request.method == 'DELETE':
        print('----------------------------------------------------')
        data = request.data
        try:
            obj = Person.objects.get(id = data['id'])
            print(obj)
            obj.delete()
            return Response({
                'msg' : 'Data has been deleted comppletely from database'
            })
        except: 
            return Response({
                "msg" : "Something went wrong with input DATA"
            })

    
    return Response({
        'msg' : 'hit the correct method DELETE'
    })

@api_view(['POST'])
def login(request):
    data = request.data
    serializer = LoginSerializer(data=data)
    if serializer.is_valid():
        return Response({
            "msg": "success"
        })
    return Response(serializer.errors)

class testingAPI(APIView):
    """
    testing api
    """

    def get(self, request):
        """
        GET method
        """
        objs = Person.objects.all()
        print(objs)
        serializer = PeopleSerializer(objs, many=True)
        return Response(serializer.data)
    

    def post(self, request):
        """
        POST method
        """
        data = request.data
        print(data)
        serializer = PeopleSerializer(data=data)
        print(serializer)
        print("*********************")
        if serializer.is_valid():
            print("yes...")
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def put(self, request):
        """
        PUT method
        """
        data = request.data
        serializer = PeopleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def patch(self, request):
        """
        FATCH method
        """
        data = request.data
        obj = Person.objects.get(id = data['id'])
        serializer = PeopleSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
    def delete(self, request):
        """
        DELETE method
        """
        data = request.data
        try:
            obj = Person.objects.get(id = data['id'])
            print(obj)
            obj.delete()
            return Response({
                'msg' : 'Data has been deleted comppletely from database'
            })
        except: 
            return Response({
                "msg" : "Something went wrong with input DATA"
            })
    
