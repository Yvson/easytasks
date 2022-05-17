from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.utils.translation import gettext_lazy as _
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template import loader

from .tokens import account_activation_token

from .models import Profile

from .forms import UserRegistrationForm, UserEditForm


def register(request):
    html_email_template_name = 'registration/acc_activate_email_html.html'    
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.is_active = False
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            current_site = get_current_site(request)
            mail_subject = _('Ative a sua conta Easytasks.')
            context = {
                'user': new_user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(new_user.pk)),
                'token': account_activation_token.make_token(new_user),
                'site_name': current_site.name,
                'protocol': 'https' if request.is_secure() else 'http'
            }
            message = render_to_string('registration/acc_activate_email_plain.html', context)
            to_email = user_form.cleaned_data.get('email')
            html_email = loader.render_to_string(html_email_template_name, context)
            email = EmailMultiAlternatives(mail_subject, message, to=[to_email])
            email.attach_alternative(html_email, 'text/html')
            email.send()
            return render(request,
                          'registration/activation_email_sent.html',
                          {'new_user': new_user})
    else:
        # If the user is logged, it must be logged out.
        if request.user.is_authenticated:
            logout(request)
        user_form = UserRegistrationForm()
    return render(request,
                  'conta/register.html',
                  {'user_form': user_form})

# Testing purposes
def register_done(request):
    context = {
        'new_user': {
            'first_name': 'New User',
        },
    }
    return render(request, 'conta/register_done.html', context)

@login_required
def profile_view(request):
    template_view = 'conta/profile.html'
    user = get_object_or_404(User, id=request.user.id)

    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=user)
        if user_form.is_valid():
            # Avoiding username change and save
            user_form.save()
            messages.success(request, 'Dados atualizados com sucesso!')
            return HttpResponseRedirect(reverse('profile_view'))
        else:
            messages.error(
                request, 'Algum problema aconteceu e os dados não foram atualizados.')

    else:
        user_form = UserEditForm(instance=user)

    context = {
        'user_form': user_form,
        'page': 'conta',
        'section': 'profile',
    }

    return render(request, template_view, context)


@login_required
def profile_delete(request):
    template_view = 'conta/profile_delete.html'
    user = get_object_or_404(User, id=request.user.id)

    if request.method == 'POST':
        user.delete()
        return HttpResponseRedirect(reverse('profile_delete_done'))

    context = {
        'page': 'conta',
        'section': 'profile',
    }
    return render(request, template_view, context)

def profile_delete_done(request):
    template_view = 'conta/profile_delete_done.html'
    context = {
        'page': 'conta',
        'section': 'profile',
    }
    if not request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('profile_delete'))

    return render(request, template_view, context)


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user, backend=settings.AUTHENTICATION_BACKENDS[0])

        context = {
            'user': user,
        }
        return render(request, 'registration/activation_done.html', context)
    else:
        return render(request, 'registration/activation_invalid.html')