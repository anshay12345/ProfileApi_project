from rest_framework import serializers
from project_api import models


class HelloSerializer(serializers.Serializer):
    """Serialize a name field for testing our APiView"""
    name = serializers.CharField(max_length=10)


# creatng model serializer which will provide some bunch of extra functionality on the existing model
class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    # we use a meta class to configure the serializer to a specific model
    class Meta:
        model = models.UserProfile  # this set our serializer up to point to our user profile model
        # now we define the list of fields we want to be accessible in our api or we want to use to create new models
        # with our serializer
        fields = ('id', 'email', 'name',
                  'password')  # password is an exception here since we will need password only while creating the
        # new user
        extra_kwargs = {  # here the keys will be the fields which we want to add the custom configuration to
            'password': {
                'write_only': True,  # we can only use it to create, we cant use it to retrieve objects
                'style': {'input_type': 'password'}  # so that when we enter the password it appears like star
            }
        }

    # Now we will create the user function instead of using the default one
    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user

    # from the class meta the required data is taken in all the fields mentioned and then we use the function create
    # which receives the validated data from above and the a user is created using create_user functtion defined in
    # the model and finally that user is returned
