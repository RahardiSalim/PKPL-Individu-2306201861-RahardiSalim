from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from .models import User


@login_required
def home_view(request):
    return render(request, 'home.html')

@login_required
def user_form_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()  # Simpan ke database
            return redirect('user_list')  # Redirect ke halaman list pengguna
    else:
        form = UserForm()
    
    return render(request, 'form.html', {'form': form})

@login_required
def user_list_view(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})
