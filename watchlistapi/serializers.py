from rest_framework import serializers
from .models import Stock
from django.contrib.auth.models import User

class StockSerializer(serializers.ModelSerializer):
    add_date = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Stock
        fields = ['id', 'name', 'symbol','add_date', 'describe']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)


    class Meta:
        model = User
        fields = ['username', 'password', 'password2']

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('Hasła nie są takie same')
        return data

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
