from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Sum
from django.core.mail import send_mail
from django.conf import settings
from .models import User, OTP, Expense
from .serializers import ExpenseSerializer, UserSerializer
import datetime

def send_otp_email(email, code, name):
    try:
        subject = '🔐 Your SpendWise OTP Code'
        html_message = f'''
<div style="font-family:Arial,sans-serif;max-width:520px;margin:0 auto;background:#07080d;color:#f4f3fa;padding:40px;border-radius:16px;border:1px solid #222">
  <div style="margin-bottom:24px">
    <span style="font-size:24px;font-weight:800;color:#4ade80">💸 SpendWise</span>
  </div>
  <h2 style="font-size:20px;margin-bottom:8px">Hi {name}, verify your login</h2>
  <p style="color:#a8a6bc;margin-bottom:24px">Use this OTP code to complete your sign in. It expires in 10 minutes.</p>
  <div style="background:#1a1e28;border:2px solid #4ade80;border-radius:12px;padding:28px;text-align:center;margin-bottom:24px">
    <div style="font-size:13px;color:#6b6882;margin-bottom:8px;letter-spacing:1px;text-transform:uppercase">Your OTP Code</div>
    <div style="font-size:42px;font-weight:700;letter-spacing:14px;color:#4ade80;font-family:monospace">{code}</div>
  </div>
  <p style="color:#6b6882;font-size:13px">⚠️ Never share this code. SpendWise will never ask for it.</p>
  <p style="color:#6b6882;font-size:13px">If you did not request this, ignore this email.</p>
</div>
'''
        send_mail(
            subject=subject,
            message=f'Hi {name},\n\nYour SpendWise OTP is: {code}\n\nExpires in 10 minutes.',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
            html_message=html_message,
            fail_silently=False,
        )
        return True
    except Exception as e:
        print(f'❌ Email error: {e}')
        return False


class RegisterView(APIView):
    def post(self, request):
        name = request.data.get('name', '').strip()
        email = request.data.get('email', '').strip().lower()
        phone = request.data.get('phone', '').strip()
        password = request.data.get('password', '')
        if not name or not email or not password:
            return Response({'error': 'All fields required'}, status=400)
        if len(password) < 6:
            return Response({'error': 'Password must be at least 6 characters'}, status=400)
        if User.objects.filter(email=email).exists():
            return Response({'error': 'Email already registered'}, status=400)
        user = User(name=name, email=email, phone=phone)
        user.set_password(password)
        user.save()
        otp = OTP.generate(email)
        email_sent = send_otp_email(email, otp.code, name)
        return Response({
            'message': 'Registered! Check your email for OTP.',
            'email_sent': email_sent,
            'email': email,
            'otp': otp.code  # remove this line after testing
        })


class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email', '').strip().lower()
        password = request.data.get('password', '')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'Invalid email or password'}, status=401)
        if not user.verify_password(password):
            return Response({'error': 'Invalid email or password'}, status=401)
        otp = OTP.generate(email)
        email_sent = send_otp_email(email, otp.code, user.name)
        return Response({
            'message': 'OTP sent to your email!',
            'email_sent': email_sent,
            'email': email,
            'otp': otp.code  # remove this line after testing
        })


class VerifyOTPView(APIView):
    def post(self, request):
        email = request.data.get('email', '').strip().lower()
        code = request.data.get('otp', '').strip()
        try:
            otp = OTP.objects.filter(email=email, code=code, is_used=False).latest('created_at')
        except OTP.DoesNotExist:
            return Response({'error': 'Invalid OTP'}, status=400)
        if not otp.is_valid():
            return Response({'error': 'OTP expired. Please login again.'}, status=400)
        otp.is_used = True
        otp.save()
        user = User.objects.get(email=email)
        return Response({'message': 'Login successful!', 'user': UserSerializer(user).data})


class ExpenseListCreateView(APIView):
    def get(self, request):
        user_id = request.query_params.get('user_id')
        qs = Expense.objects.filter(user_id=user_id) if user_id else Expense.objects.all()
        return Response(ExpenseSerializer(qs.order_by('-created_at'), many=True).data)

    def post(self, request):
        s = ExpenseSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=201)
        return Response(s.errors, status=400)


class ExpenseDetailView(APIView):
    def get_object(self, pk):
        try:
            return Expense.objects.get(pk=pk)
        except Expense.DoesNotExist:
            return None

    def get(self, request, pk):
        e = self.get_object(pk)
        return Response(ExpenseSerializer(e).data) if e else Response({'error': 'Not found'}, status=404)

    def put(self, request, pk):
        e = self.get_object(pk)
        if not e:
            return Response({'error': 'Not found'}, status=404)
        s = ExpenseSerializer(e, data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data)
        return Response(s.errors, status=400)

    def delete(self, request, pk):
        e = self.get_object(pk)
        if not e:
            return Response({'error': 'Not found'}, status=404)
        e.delete()
        return Response({'message': 'Deleted'}, status=204)


class AnalyticsView(APIView):
    def get(self, request):
        user_id = request.query_params.get('user_id')
        qs = Expense.objects.filter(user_id=user_id) if user_id else Expense.objects.all()
        total = qs.aggregate(t=Sum('amount'))['t'] or 0
        by_cat = list(qs.values('category').annotate(total=Sum('amount')).order_by('-total'))
        monthly = list(
            qs.extra(select={'month': "DATE_FORMAT(date, '%%Y-%%m')"})
            .values('month').annotate(total=Sum('amount')).order_by('month')
        )
        return Response({'total_spent': total, 'by_category': by_cat, 'monthly': monthly})


class ProfileView(APIView):
    def get(self, request, user_id):
        try:
            user = User.objects.get(pk=user_id)
            count = Expense.objects.filter(user=user).count()
            total = Expense.objects.filter(user=user).aggregate(t=Sum('amount'))['t'] or 0
            return Response({
                **UserSerializer(user).data,
                'expense_count': count,
                'total_spent': total
            })
        except User.DoesNotExist:
            return Response({'error': 'Not found'}, status=404)