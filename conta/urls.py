from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from . import views, forms

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
            authentication_form=forms.LoginForm,
            redirect_authenticated_user=True,
        ), 
        name="login"
    ),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('seguranca/', auth_views.PasswordChangeView.as_view(
        template_name = 'conta/security.html',
        extra_context = {
            'section': 'password',
            'page': 'conta',
        }),
        name='password_change'
    ),
    path('seguranca/feito/', auth_views.PasswordChangeDoneView.as_view(
            template_name='conta/security_done.html'
        ),
        name='password_change_done'
    ),
    path('recuperar/', 
        auth_views.PasswordResetView.as_view(
            template_name='registration/recovery.html',
            email_template_name = 'registration/reset_email_plain.html',
            html_email_template_name= 'registration/reset_email_html.html',
            ), 
        name='password_reset'
    ),
    path('recuperar/feito/', auth_views.PasswordResetDoneView.as_view(
            template_name='registration/recovery_done.html'
        ),
        name='password_reset_done'
    ),
    path('resetar/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
            template_name='registration/reset.html'
        ),
        name='password_reset_confirm'
    ),
    path('resetar/feito/', auth_views.PasswordResetCompleteView.as_view(
            template_name='registration/reset_done.html'
        ),
        name='password_reset_complete'
    ),
    
    path('cadastro/', views.register, name="register"),
    #path('cadastro/feito/', views.register_done, name="register"), # Only for tests
    path('perfil/', views.profile_view, name='profile_view'),
    path('perfil/excluir/', views.profile_delete, name='profile_delete'),
    path('perfil/excluir/feito/', views.profile_delete_done, name='profile_delete_done'),
    re_path(r'^ativacao/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]+-[0-9A-Za-z]+)/$',
        views.activate, name='activate_view')    
    
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)