from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers

class ProductsApiview(APIView):
    serializer_class = serializers.ProductsSerializers

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






