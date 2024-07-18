"""
View.py
"""

# for class views
from rest_framework.decorators import api_view
# for responding 
from rest_framework.response import Response
from rest_framework import viewsets
from home.models import Person
from home.serializer import PeopleSerializer, LoginSerializer, RegisterSerializer
from rest_framework.views import APIView

# for responding errors
from rest_framework import status

# for registrations and login 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

#for token verification and all
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


# for pagination
from  django.core.paginator import Paginator

#for action in django 
from rest_framework.decorators import action


class LoginAPI(APIView):
    """
    Login class
    """

    def post(self, request):
        data = request.data
        serializer = LoginSerializer(data=data)

        if not serializer.is_valid():
            return Response(
                {"msg": serializer.errors, "status": False}, status.HTTP_400_BAD_REQUEST
            )

        user = authenticate(
            username=serializer.data["username"], password=serializer.data["password"]
        )

        if not user:
            return Response({
                'msg': 'Invalid credentials',
                'status': False,
            }, status.HTTP_404_NOT_FOUND)
        
        token, _ = Token.objects.get_or_create(user=user)

        return Response(
            {"sataus": True, "user": "login", "token": str(token)},
            status.HTTP_201_CREATED,
        )


class RegisterAPI(APIView):
    """
    Registration API
    """

    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)

        if not serializer.is_valid():
            return Response(
                {"status": False, "message": serializer.errors},
                status.HTTP_400_BAD_REQUEST,
            )

        serializer.save()
        return Response(
            {"status": True, "msg": serializer.data}, status.HTTP_201_CREATED
        )


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
        obj = Person.objects.get(id=data["id"])
        serializer = PeopleSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response({"message": "Hit a PUT request"})


@api_view(["GET", "POST", "PUT", "DELETE"])
def delete_data(request):

    if request.method == "DELETE":
        print("----------------------------------------------------")
        data = request.data
        try:
            obj = Person.objects.get(id=data["id"])
            print(obj)
            obj.delete()
            return Response({"msg": "Data has been deleted comppletely from database"})
        except:
            return Response({"msg": "Something went wrong with input DATA"})

    return Response({"msg": "hit the correct method DELETE"})


@api_view(["POST"])
def login(request):
    data = request.data
    serializer = LoginSerializer(data=data)
    if serializer.is_valid():
        return Response({"msg": "success"})
    return Response(serializer.errors)


class testingAPI(APIView):
    """
    testing api
    """

    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        """
        GET method
        """
        try:
            print(request.user)  # which user is logedin
            objs = Person.objects.all()
            page = request.GET.get('page', 1)
            page_size = 3
            paginator = Paginator(objs, page_size)
            print(objs)
            serializer = PeopleSerializer(paginator.page(page), many=True)
            return Response(serializer.data)
        
        except Exception as e:
            return Response({
                'status' : False,
                'message': 'Invalid Page'
            })
        

        



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
        obj = Person.objects.get(id=data["id"])
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
            obj = Person.objects.get(id=data["id"])
            print(obj)
            obj.delete()
            return Response({"msg": "Data has been deleted comppletely from database"})
        except:
            return Response({"msg": "Something went wrong with input DATA"})


# Handle all the CRUD APIs by using model view set
class PeopleViewSet(viewsets.ModelViewSet):
    serializer_class = PeopleSerializer
    queryset = Person.objects.all()

    def list(self, request):
        search = request.GET.get("search")
        queryset = self.queryset
        try:
            print(queryset)
            if search:
                queryset = queryset.filter(name__startswith=search)

            serializer = PeopleSerializer(data=queryset, many=True)
            print(serializer.is_valid())
            return Response({"message": "success", "data": serializer.data})
            
        except Exception as e:
            return Response({"message": "Failed"})


    @action(detail=False, methods=['get'])
    def send_get_email(self, request):
        print(request.data)
        print("this is get request")
        return Response({
            'msg' : "thanx for visiting our API"
        })
