# -*- coding: utf-8 -*-
from django.contrib.auth.models import User, Group
from rest_framework import serializers
#importar los modelos creados
#from servi.express.models import 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


   
