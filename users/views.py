from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer, UserSerializer

User = get_user_model()


# ✅ 회원가입 API (JWT 토큰 반환)
class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]  # 누구나 접근 가능

    def perform_create(self, serializer):
        """회원가입 및 JWT 토큰 생성"""
        try:
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            self.response_data = {
                "message": "회원가입 성공",
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }
        except Exception as e:
            self.response_data = {"error": f"회원가입 중 오류 발생: {str(e)}"}

    def create(self, request, *args, **kwargs):
        """회원가입 요청 처리 및 응답"""
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(self.response_data, status=status.HTTP_201_CREATED)
        print("❌ 회원가입 오류:", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ✅ 로그인한 사용자 정보 조회 API
class UserDetailView(RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        """현재 로그인한 사용자만 반환"""
        return self.request.user
