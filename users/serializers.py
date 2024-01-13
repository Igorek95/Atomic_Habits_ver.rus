

from rest_framework import serializers

from users.models import User


class UserSerializerPrivateUpdate(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()
        return instance


class UserSerializerPublic(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class UserSerializerPrivateDetails(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'date_joined']
