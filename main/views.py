from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


# Create your views here.
def main(request):
    # return HttpResponse('<h1>Hello</h1>')
    return render(request, 'main_page.html')


# def post_number(request, number: int):
#     return HttpResponse(f'<h1>Post #{number}</h1>')
#
#
# def post_number_month(request, number: int, month: int):
#     if 1 <= month <= 12:
#         return HttpResponse(f'<h1>Post #{number} from month #{month}</h1>')
#     return HttpResponseNotFound('Wrong month')
