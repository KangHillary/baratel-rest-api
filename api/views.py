from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from . import permissions

from . import serializers, models

class ProfilesApiview(APIView):
    serializer_class = serializers.ProfilesSerializers

    def get(self,request,format=None):
        an_apiview = [
            'Oranges',
            'Mangoes',
            'Banana'

        ]
        return Response({'message':'continental fruits','an_apiview':an_apiview})

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello, {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.error_messages,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self,request,pk=None):
        """ handle updating an existing object """
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        '''handle partial update'''
        return Response({'method':'patch'})

    def delete(self,request,pk=None):
        '''Delete an object in db'''
        return Response({'method':'delete'})


class ProfileViewset(viewsets.ViewSet):
    serializer_class = serializers.ProfilesSerializers

    def list(self,request):
        a_viewset = [
            'uses actions(list,update,create,retrieve,partial_update',
            'Automatically maps to urls sing routers',
            'uses less code'
        ]
        return Response({'message':'My list viewset','viewset':a_viewset})

    def create(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello, {name}!'
            return Response({'message':message})
        else:
            return Response(
                serializer.error_messages,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self,request,pk=None):
        '''Handle get object by ID'''
        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        '''Handle get object by ID'''
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        '''Handle update part of an object'''
        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        '''Handle remove an object'''
        return Response({'http_method':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """handle create and update user profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.Userprofile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields =('name','email',)


class UserLoginApiView(ObtainAuthToken):
   """Handle creating user authentication tokens"""
   renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES








