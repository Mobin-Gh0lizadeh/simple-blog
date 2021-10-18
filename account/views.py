from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login


class UserLogin(auth_views.LoginView):
	template_name = 'account/login.html'

class UserPassReset(auth_views.PasswordResetView):
	template_name = 'account/password_reset_form.html'
	success_url = reverse_lazy('account:password_reset_done')
	email_template_name = 'account/password_reset_email.html'

class PasswordResetDone(auth_views.PasswordResetDoneView):
	template_name = 'account/reset_done.html'

class PasswordResetConfirm(auth_views.PasswordResetConfirmView):
	template_name = 'account/password_reset_confirm.html'
	success_url = reverse_lazy('account:password_reset_complete')

class PasswordResetComplete(auth_views.PasswordResetCompleteView):
	template_name = 'account/password_reset_complete.html'

def user_register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = User.objects.create_user(cd['username'], cd['email'], cd['password'])
			login(request, user)
			messages.success(request, 'You Registered Successfully', 'success')
			return redirect('/')
	else:
		form = RegisterForm()
	return render(request, 'account/register.html', {'form':form})