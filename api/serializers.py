from rest_framework import serializers


class ProductsSerializers(serializers.Serializer):
    """a serializer to test products view"""
    name = serializers.CharField(max_length=10)




