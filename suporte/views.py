from django.views.generic.base import TemplateView
from django.urls import reverse
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.contrib import messages


from .forms import ContactForm


class AboutTemplateView(TemplateView):
    template_name = 'suporte/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = 'suporte'
        context["section"] = 'sobre'
        return context
    

class TermsTemplateView(TemplateView):
    template_name = 'suporte/terms.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = 'suporte'
        context["section"] = 'termos'
        return context

class ConductTemplateView(TemplateView):
    template_name = 'suporte/conduct.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = 'suporte'
        context["section"] = 'conduta'
        return context

class PrivacyTemplateView(TemplateView):
    template_name = 'suporte/privacy.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = 'suporte'
        context["section"] = 'privacidade'
        return context

class ContactTemplateView(TemplateView):
    template_name = 'suporte/contact.html'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = 'suporte'
        context["section"] = 'contato'
        context["form"] = ContactForm()
        return context

    def post(self, request):
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            cd = contact_form.cleaned_data
            name = cd['name']
            email = cd['email']
            subject = f"{name} - Contato Easytasks"
            message = f"Sender: {email}\nMessage: {cd['message']}"
            
            send_mail(
                subject=subject,
                from_email=email,
                recipient_list=['yvsonexs@gmail.com'],
                message=message,
            )
            return HttpResponseRedirect(reverse('contact_sent_view'))
        else:
            messages.error('Algum problema aconteceu. Por favor, tentar novamente.')
            return HttpResponseRedirect(reverse('contact_view'))
        
    
class ContactSentTemplateView(TemplateView):
    template_name = 'suporte/contact_sent.html'



