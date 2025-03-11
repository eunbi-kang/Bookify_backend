from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, UserDetailView

urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="login"),  # ✅ 로그인 (JWT 발급)
    path("register/", RegisterView.as_view(), name="register"),  # ✅ 회원가입
    path("me/", UserDetailView.as_view(), name="user-detail"),  # ✅ 로그인한 사용자 정보 조회
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),  # ✅ JWT 갱신
]
