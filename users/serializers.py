from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import CustomUser

# ✅ 회원가입 Serializer
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = CustomUser
        fields = ("username", "email", "password", "phone", "profile_image", "address", "date_of_birth")

    def create(self, validated_data):
        # ✅ 비밀번호 자동 해싱
        user = CustomUser.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],  # Django 내부에서 해싱 처리
            phone=validated_data.get("phone"),
            profile_image=validated_data.get("profile_image"),
            address=validated_data.get("address"),
            date_of_birth=validated_data.get("date_of_birth"),
        )
        return user


# ✅ 사용자 정보 Serializer (비밀번호 X)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username", "email", "phone", "profile_image", "address", "date_of_birth"]
