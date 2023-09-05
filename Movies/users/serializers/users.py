from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import ParseError

# from Movies.users.backend import User
from ..backend import User # it's work with docker!


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'password',
        )

    def validate_email(self, value):
        email = value.lower()
        if User.objects.filter(email=email).exists():
            raise ParseError(f"User with email:{email} exists")
        return email

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)


    class Meta:
        model = User
        fields = ('old_password', 'new_password')

    def validate(self, attrs):
        user = self.instance
        old_password = attrs.pop('old_password')
        if not user.check_password(old_password):
            raise ParseError('Проверьте правильность пароля.')

        return attrs

    def validate_new_password(self, value):
        validate_password(value)
        return value

    def update(self, instance, validated_data):
        password = validated_data.get('new_password')
        instance.set_password(password)
        instance.save()
        return instance


class MeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = (
        #     'id',
        #     'first_name',
        #     'last_name',
        #     'email',
        #     'date_joined',
        # )
        fields = '__all__'

class MeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
        )

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)

        # тут можно обновлять связи, пример кода:
        # some_data = ...
        # relation_name = instance.relation_name
        # for key, value in some_data:
        #     if hasattr(rerelation_name, key):
        #         setattr(rerelation_name, key, value)
        # rerelation_name.save()

        return instance