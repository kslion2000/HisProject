from django.shortcuts import render
import requests
from register.forms import *


# Create your views here.
def index(request):
    response = requests.get(
        "https://emma.pixnet.cc/mainpage/blog/categories/hot/33")
    articles = response.json()["articles"] #轉換為JSON物件後，存取articles欄位
    return render(request, "posts/index.html", {"articles": articles})

def resign_page(request):
    return render(request, 'register/resign_page.html')

def crate_patient(request):
    patient_info = PatientInformationForm()
    return render(request, 'register/crate_patient.html')