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

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "message": "회원가입 성공",
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                },
                status=status.HTTP_201_CREATED,
            )
        print("❌ 회원가입 오류:", serializer.errors)  # ✅ 추가: 에러 로그 출력
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ✅ 로그인한 사용자 정보 조회 API
class UserDetailView(RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  # 로그인
