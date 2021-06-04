from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
# status here is a set of handy HTTP status code that we can use when returning responses from our api
from project_api import serializers, models
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from project_api import permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

# when django rest_framework calls the api view, it is expecting to return this standard Response object
class HelloApiView(APIView):
    """Api view class"""
    serializer_class = serializers.HelloSerializer  # When ever we make a put, post or patch request, we

    # are gonna expect an input field name which will be validated with the max_length=10
    def get(self, request, format=None):
        """Return a list of APIView features"""
        # The way API view are broken up is to expects a function for different HTTP request that can
        # be made to the view, when we make a http get request to the url that it will be assigned to this
        # class, it will call this get function and will execute the logic written in the get fucntion
        # here format parameter add a format suffix to the end of the endpoint URL
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, deleter)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to Urls',
        ]

        return Response({'message': 'Hello World', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)  # retreiving data from the request using the
        # help of  serializer_class

        if serializer.is_valid():  # checking the validation(max_length=10)
            name = serializer.validated_data.get('name')  # getting the name
            message = f'Hello {name}'  # displaying the name
            return Response({'message': message})

        else:  # what if max_length>10
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):  # pk will take the id of the objcet to be updated with the put request
        """Handling updating an object"""
        # when ever we made a put request, it will update that object with the data provided in the request
        # when we are doing HTTp put we typically do it to a specific URL primary key
        # HTTP PUT IS ESSENTIALLY REPLACING AN OBJECT WITH THE OBJECT THAT WAS PROVIDED
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partiol update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        return Response({'method': 'Delete'})


# FROM HERE THE VIEWSET STARTS
class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Returns a Hello message"""
        a_viewset = [
            'User actions(list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using routers',
            'Provide more functionality with less code',
        ]

        return Response({'message': 'Hello!', 'view_set': a_viewset})

    def create(self, request):
        """create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')  # now getting the name from the serializer_class
            message = f'Hello {name}!'
            return Response({'messsage': message})

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    # retrieve function is for retrieveing a specific object in our viewset, so we would
    # typically pass in a primary key ID to the URL in the request,
    # and that will return the object with that primary key ID.
    def retrieve(self, request, pk=None):
        """handle getting an object by its ID"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """handle updating part of an object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """handle removing an object"""
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    # ',' is added to make sure that the python knows that this is not a sngle item, instead it is a tuple
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = {'name', 'email', }  # this means that the DRF will allow us to search for items in this view set
    # by the name or email field


class UserLoginApiView(ObtainAuthToken):
    # ObtainAuthToken is the class provided by the DRF and we could just add it directly to a URLs dot by file
    # however it doesn't by default enables itself in the browsable Django admin site so we need to override this
    # class and customize it so it's visible in the browsable api so it makes it easier for us to test
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
