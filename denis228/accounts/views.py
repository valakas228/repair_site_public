from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from .forms import CustomAuthenticationForm, CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from store.models import RepairRequest
from store.forms import AdminResponseForm
from django.contrib.admin.views.decorators import staff_member_required

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('main')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            username_or_email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username_or_email, password=password)
            if user is not None:
                login(request, user)
                return redirect('main')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def profile(request):
    user = request.user
    repair_requests = RepairRequest.objects.filter(user=user).order_by('-created_at')
    admin_repair_requests = None
    if user.is_staff:
        admin_repair_requests = RepairRequest.objects.all().order_by('-created_at')
    return render(request, 'accounts/profile.html', {
        'user': user,
        'repair_requests': repair_requests,
        'admin_repair_requests': admin_repair_requests
    })

def logout_view(request):
    logout(request)
    return redirect('main')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {'form': form})

def is_admin(user):
    return user.is_staff

@user_passes_test(is_admin)
def admin_dashboard(request):
    repair_requests = RepairRequest.objects.all().order_by('-created_at')
    return render(request, 'accounts/admin_dashboard.html', {'repair_requests': repair_requests})

@staff_member_required
def delete_repair_request(request, request_id):
    repair_request = get_object_or_404(RepairRequest, id=request_id)
    if request.method == 'POST':
        repair_request.delete()
        messages.success(request, 'Заявка успешно удалена!')
        return redirect('profile')
    return render(request, 'accounts/delete_repair_request.html', {'repair_request': repair_request})

@staff_member_required
def edit_repair_request(request, request_id):
    repair_request = get_object_or_404(RepairRequest, id=request_id)
    if request.method == 'POST':
        form = AdminResponseForm(request.POST, instance=repair_request)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ответ успешно сохранен!')
            return redirect('profile')
    else:
        form = AdminResponseForm(instance=repair_request)
    return render(request, 'accounts/edit_repair_request.html', {'form': form, 'repair_request': repair_request})