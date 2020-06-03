from rest_framework.views import APIView
from rest_framework.response import Response


class ProductsApiview(APIView):

    def get(self,request,format=None):
        an_apiview = [
            'Oranges',
            'Mangoes',
            'Banana'

        ]

        return Response({'message':'continental fruits','an_apiview':an_apiview})


