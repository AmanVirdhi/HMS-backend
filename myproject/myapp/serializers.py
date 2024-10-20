from rest_framework import serializers  
from .models import Grievance, User, Signup
# from .models import *  //for all modals
# serializers is package

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        # fields = ['name', 'age']

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signup
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        # Create a new user instance and save it to the database
        user = Signup(**validated_data)  # The password will be hashed in the model's save method
        user.save()
        return user  

class GrievanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grievance
        fields = '__all__'       

   