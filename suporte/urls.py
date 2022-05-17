from django.urls import path
from .views import AboutTemplateView 
from .views import TermsTemplateView
from .views import ConductTemplateView
from .views import PrivacyTemplateView
from .views import ContactTemplateView, ContactSentTemplateView


urlpatterns = [
    path('sobre/', AboutTemplateView.as_view(), name="about_view"),
    path('termos/', TermsTemplateView.as_view(), name="terms_view"),
    path('privacidade/', PrivacyTemplateView.as_view(), name="privacy_view"),
    path('contato/', ContactTemplateView.as_view(), name="contact_view"),
    path('contato/enviado/', ContactSentTemplateView.as_view(), name="contact_sent_view"),
]
