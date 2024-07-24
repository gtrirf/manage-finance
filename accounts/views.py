from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RegisterForm, LoginForm, ProfileUpdateForm, VerificationForm
from .models import CustomUser as User
from django.core.mail import send_mail
from django.conf import settings
from .models import VerificationCode


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'accounts/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('charts-home')
        return render(request, 'accounts/login.html', {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'accounts/profile.html', {'user': request.user})


class ProfileUpdateView(LoginRequiredMixin, View):
    def get(self, request):
        form = ProfileUpdateForm(instance=request.user)
        return render(request, 'accounts/profile_edit.html', {'form': form})

    def post(self, request):
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        return render(request, 'accounts/profile_edit.html', {'form': form})


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'accounts/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password1'],
                fullname=form.cleaned_data.get('fullname', '')
            )
            verification_code = VerificationCode.objects.create(user=user)
            verification_code.generate_code()

            send_mail(
                'Verify Your Email',
                f'Your verification code is {verification_code.code}',
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=False,
            )

            request.session['email'] = user.email
            return redirect('verify-email')

        return render(request, 'accounts/register.html', {'form': form})


class VerifyEmailView(View):
    def get(self, request):
        form = VerificationForm()
        return render(request, 'accounts/verify_email.html', {'form': form})

    def post(self, request):
        form = VerificationForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            email = request.session.get('email')
            try:
                verification_code = VerificationCode.objects.get(code=code, user__email=email)
                if verification_code.is_valid():
                    user = verification_code.user
                    user.is_active = True
                    user.save()
                    verification_code.delete()
                    del request.session['email']
                    return redirect('login')
                else:
                    form.add_error(None, 'The code has expired')
            except VerificationCode.DoesNotExist:
                form.add_error(None, 'Invalid code')
        return render(request, 'accounts/verify_email.html', {'form': form})
