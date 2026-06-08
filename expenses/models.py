import datetime
from django.db import models
from django.contrib.auth.hashers import make_password, check_password
import random, datetime

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def set_password(self, raw):
        self.password = make_password(raw)

    def verify_password(self, raw):
        return check_password(raw, self.password)

    def __str__(self):
        return self.email

class OTP(models.Model):
    email = models.EmailField()
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    is_used = models.BooleanField(default=False)

    def is_valid(self):
        expiry = self.created_at + datetime.timedelta(minutes=10)
        return not self.is_used and datetime.datetime.now(datetime.timezone.utc) < expiry

    @staticmethod
    def generate(email):
        OTP.objects.filter(email=email, is_used=False).update(is_used=True)
        code = str(random.randint(100000, 999999))
        return OTP.objects.create(email=email, code=code)

class Expense(models.Model):
    CATEGORIES = [
        ('Food', 'Food'), ('Travel', 'Travel'),
        ('Shopping', 'Shopping'), ('Bills', 'Bills'),
        ('Health', 'Health'), ('Education', 'Education'), ('Other', 'Other'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses')
    category = models.CharField(max_length=50, choices=CATEGORIES)
    description = models.TextField(blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(default=datetime.date.today)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.name} - {self.category} - {self.amount}"