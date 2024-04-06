from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "date_joined"]
        read_only_fields = ["date_joined"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )

    def update(self, instance, validated_data):
        password = validated_data.get("password", instance.password)
        if not instance.check_password(password):
            raise serializers.ValidationError(
                {
                    "password": _("Password is not correct"),
                },
            )
        instance.username = validated_data.get("username", instance.username)
        instance.email = validated_data.get("email", instance.email)
        instance.save()
        return instance


class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        required=True,
        style={"input_type": "password", "placeholder": "Old password"},
    )
    new_password = serializers.CharField(
        required=True,
        style={"input_type": "password", "placeholder": "New password"},
    )
    new_password_confirm = serializers.CharField(
        required=True,
        style={"input_type": "password", "placeholder": "Сonfirm password"},
    )

    def validate(self, attrs):
        if attrs["new_password"] != attrs["new_password_confirm"]:
            raise serializers.ValidationError(
                {
                    "password": _("Password fields didn't match"),
                },
            )
        return attrs
