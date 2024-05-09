from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
import csv
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')
def about(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'about.html')
def contact(request):
    if request.user.is_anonymous:
        return redirect("/login")
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        contact = Contact(fname=fname, lname=lname, email=email, comment=comment, date=datetime.today())
        contact.save()
        messages.success(request, 'Successfully Sent!')
    return render(request, 'contact.html')
def loginUser(request):                         #passkey:nIY6sFNLk3ZV9
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
    return render(request, 'login.html')
def logoutUser(request):
    logout(request)
    return redirect("/login")
def filter_scholarships(request):
    filters = {}
    gender = request.POST.get('gender')
    country = request.POST.get('country')
    education = request.POST.get('educationField')
    annual_income = request.POST.get('annualIncome')
    minorities = request.POST.get('minorities')
    scholarsips = []
    with open('D:\Scholarship Recommendation Website\Scholarship_Recommendation_Website\home\Scholarshipsnew.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            scholarsips.append(row)
    for scholarship in scholarsips:
        if minorities and scholarship['Minorities'] != minorities:
            continue
        if education and scholarship['Education'] != education:
            continue
        if annual_income and scholarship['Annual Income'] != annual_income:
            continue
        if gender and scholarship['Gender'] != gender:
            continue
        if country and scholarship['Country'] != country:
            continue
        filters[scholarsips['Sr_No']] = scholarsips
    return render(request, 'filter_scholarships.html', {'filters':filters})