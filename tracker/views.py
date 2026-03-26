from django.shortcuts import render
from .models import College
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def college_search(request):
    query = request.GET.get('q', '')
    colleges = College.objects.filter(name__icontains=query) if query else College.objects.all()
    return render(request, 'tracker/college_search.html', {
        'colleges': colleges,
        'query': query
    })

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('college_search')
    else:
        form = UserCreationForm()
    return render(request, 'tracker/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('college_search')
    else:
        form = AuthenticationForm()
    return render(request, 'tracker/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

from django.contrib.auth.decorators import login_required
from .models import College, Application

@login_required(login_url='login')
def dashboard(request):
    applications = Application.objects.filter(user=request.user)
    total = applications.count()
    submitted = applications.filter(status='submitted').count()
    in_progress = applications.filter(status='in_progress').count()
    not_started = applications.filter(status='not_started').count()
    return render(request, 'tracker/dashboard.html', {
        'applications': applications,
        'total': total,
        'submitted': submitted,
        'in_progress': in_progress,
        'not_started': not_started,
    })

# Comment