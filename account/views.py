from django.shortcuts import render

# from account.models import Account


def sign_up(request):
    return render(request, 'sign_up.html')


def log_in(request):
    # if request.method == 'POST':
    #     account = Account()
    #     account.name = request.POST.get("email")
    #     account.age = request.POST.get("password")
    #     account.save()
    return render(request, 'log_in.html')


