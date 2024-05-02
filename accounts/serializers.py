from rest_framework import serializers
from .models import MyUser

class JoinSerializer(serializers.ModelSerializer):
    class Meta:
        model= MyUser
        fields= "__all__"
        
class UsernameSerializer(serializers.ModelSerializer):
    class Meta:
        model= MyUser
        fields= "__all__" 
        
    def to_representation(self, instance):
        ret= super().to_representation(instance)
        ret.pop("password")
        return ret      