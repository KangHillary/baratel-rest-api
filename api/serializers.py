from rest_framework import serializers
from . import models



class ProfilesSerializers(serializers.Serializer):
    """a serializer to test products view"""
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializing a model """
    class Meta:
        model = models.Userprofile
        fields  = ('id','email','name','password')
        extra_kwargs = {
            'password':{
                    'write_only':True,
                    'style':{
                        'input_type':'password'
                    }
            }
        }

    def create(self, validated_data):
        """Create and return created object"""
        user = models.Userprofile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']

        )
        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)


class ProfileFeedItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id','status_text','created_on','user_profile')
        extra_kwargs = {
            'user_profile':{
                'read_only':True
            }
        }




