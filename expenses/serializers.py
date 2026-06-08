from rest_framework import serializers
from .models import User, Expense

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'created_at']

class ExpenseSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.name', read_only=True)
    user_email = serializers.CharField(source='user.email', read_only=True)

    class Meta:
        model = Expense
        fields = ['id', 'user', 'user_name', 'user_email',
                  'category', 'description', 'amount', 'date', 'created_at']
        read_only_fields = ['date', 'created_at']