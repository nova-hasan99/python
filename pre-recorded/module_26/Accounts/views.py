from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from .forms import CustomAuthenticationForm, CustomPasswordResetForm, CustomUserCreationFomr
from .models import CustomUser, UserProfile
from django.views.decorators.csrf import csrf_exempt


@login_required
def user_dashboard(request):
    user = request.user
    user_profile, created = UserProfile.objects.get_or_create(user=user)
    if request.method == 'POST':
        user.username = request.POST.get('username', user.username)
        user.email = request.POST.get('email', user.email)
        user.save()

        user_profile.mobile = request.POST.get('mobile', user_profile.mobile)
        user_profile.address_line_1 = request.POST.get('address_line_1', user_profile.address_line_1)
        user_profile.address_line_2 = request.POST.get('address_line_2', user_profile.address_line_2)
        user_profile.city = request.POST.get('city', user_profile.city)
        user_profile.state = request.POST.get('state', user_profile.state)
        user_profile.country = request.POST.get('country', user_profile.country)
        user_profile.save()

        return redirect('user_dashboard')
    context = {
        'user_info' : user,
    }
    return render(request, 'Accounts/user_dashboard.html', context)
