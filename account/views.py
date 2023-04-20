from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# from account.models import Account


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


# @login_required
# def profile(request):
#     user_profile = request.user
#     context = {'user_profile': user_profile}
#     return render(request, 'profile.html', context)
#
# @login_required
# def home(request):
#     return redirect('profile')
