from django.urls import path
from .views import (RegisterView, LoginView, VerifyOTPView,
                    ExpenseListCreateView, ExpenseDetailView,
                    AnalyticsView, ProfileView)

urlpatterns = [
    path('auth/register/', RegisterView.as_view()),
    path('auth/login/', LoginView.as_view()),
    path('auth/verify-otp/', VerifyOTPView.as_view()),
    path('expenses/', ExpenseListCreateView.as_view()),
    path('expenses/<int:pk>/', ExpenseDetailView.as_view()),
    path('analytics/', AnalyticsView.as_view()),
    path('profile/<int:user_id>/', ProfileView.as_view()),
]