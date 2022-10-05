from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def read_cookies(request):
    # printing cookies
    return HttpResponse(request.COOKIES.items())


from django.core.signing import Signer
def set_a_new_secret_cookie(request):
    key = request.GET.get('key', "default")
    signer = Signer()
    secret_value = signer.sign(request.GET.get('value', ""))
    print(secret_value)
    _, value = secret_value.split(":")
    print(secret_value)
    # set a new cookie
    response = HttpResponse(request.COOKIES.items())
    response.set_cookie(key=key, value=value, max_age=1000)
    print(f"Unsigned value is - {signer.unsign(secret_value)}")
    return response

def get_session_details(request):
    session_values = request.session.items()
    print(session_values)
    return HttpResponse(session_values)

def get_session_details(request):
    session_values = request.session.items()
    print(session_values)
    return HttpResponse(session_values)

def set_session_details(request):
    key = request.GET.get('key')
    value = request.GET.get('value')
    request.session[key] = value
    return HttpResponseRedirect(reverse('student_session_details'))

def encrypt_cookie(request):
    value = request.COOKIES.get('visit', 0)
    if value:
        value = int(decrypt(value, SECRET_KEY))
    else:
        value = 0

    value += 1
    message = f"<h2>This page has been visited {value} times</h2>"
    value = encrypt(str(value), SECRET_KEY)

    response = HttpResponse(message)
    response.set_cookie(key='visit', value=value, max_age=500)
    return response



# # count user visits
# from django.views.generic.base import TemplateView
# from datetime import datetime
# from .models import PageView
#
# def index(request):
#     current_page_count = PageView.objects.filter(page=page_name).hits
#     context = {'page': current_page_count}
#
#     if not request.session.get('counted'):
#         page_view = PageView()
#         page_view.hit = current_page_count + 1
#         page_view.save()
#         context = {'page': page_view.hit}
#         request.session['counted'] = True
#
#     return render(request, 'pages/index.html', context=context)