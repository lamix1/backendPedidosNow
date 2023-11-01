from django.contrib.auth.models import User, Group
from rest_framework.serializers import ModelSerializer, ListField

class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ('name', )

class UserSerializer(ModelSerializer):
    groups = GroupSerializer(many=True)
    class Meta:
        model = User
        fields = ('id','first_name', 'username', 'groups')