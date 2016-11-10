from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as authlogin
from django.contrib.auth import authenticate
from django.views.generic import View


class login_view(View):

    def get(self, request):
        form = AuthenticationForm()
        if request.user.is_authenticated():
            return redirect('profile:profile', username=request.user.username)

        return render(request, 'user_manager/login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(request.POST)
        if request.user.is_authenticated():
            return redirect('profile:profile', username=request.user.username)

        if form.is_valid():
            user = form.get_user()
            authlogin(request, user)
            return redirect('profile:profile', username=user.username)

        return render(request, 'user_manager/login.html', {'form': form})
# def login(request):
#     if request.method == "POST":
#         form = AuthenticationForm(request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             authlogin(request, user)
#             return redirect('profile:profile', username=user.username)
#     else:
#         form = AuthenticationForm()
#
#     return render(request, 'user_manager/login.html', {'form': form})

def register(request):
    return

def forgot_pass(request):
    return