from django.shortcuts import render

# Create your views here.
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import OTP
from django.core.mail import send_mail
from django.conf import settings

def generate_otp(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.get(email=email)
        otp = OTP.generate_otp(user)
        send_mail(
            'OTP Verification',
            f'Your OTP is: {otp}',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
        return redirect('verify_otp')
    return render(request, 'generate_otp.html')
# views.py
def verify_otp(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        otp_entered = request.POST.get('otp')
        user = User.objects.get(email=email)
        otp_instance = OTP.objects.filter(user=user, otp=otp_entered).order_by('-created_at').first()
        if otp_instance:
            # OTP is correct
            otp_instance.delete()  # Delete used OTP
            # Redirect to password reset view or any other desired action
            return redirect('app/password_reset')
        else:
            # Incorrect OTP
            return render(request, 'verify_otp.html', {'error': 'Invalid OTP'})
    return render(request, 'verify_otp.html')
