from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from django.core.exceptions import ValidationError
from django.http import JsonResponse


from .forms import NumberForm, PasswordForm
from .models import Number, Password

from ast import literal_eval


class NumbersTemplateView(TemplateView):
    template_name = 'gerador/numbers.html'

    def dispatch(self, request, number_id=None, *args, **kwargs):
        self.number_id = number_id
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if (self.request.user.is_authenticated):
            context['numbers_list'] = Number.objects.filter(
                profile=self.request.user.profile)

            numbers_data = Number.objects.filter(
                profile=self.request.user.profile,
                id=self.number_id
            )
            context['numbers'] = numbers_data

        context["page"] = 'gerador'
        context["section"] = 'numeros'
        return context

    @method_decorator(login_required)
    def post(self, request):
        req = literal_eval((request.POST.get('json')))

        data = {
            'profile': self.request.user.profile,
            'numbers': req['numbers'],
            'columns': req['columns'],
        }
        savedNumber_form = NumberForm(data=data)

        if savedNumber_form.is_valid():
            clean_savedNumber = savedNumber_form.clean()
            try:
                new_savedNumber = Number(
                    profile=clean_savedNumber['profile'],
                    numbers=clean_savedNumber['numbers'],
                    columns=clean_savedNumber['columns']
                )
                try:
                    new_savedNumber.save()
                except ValidationError:
                    return JsonResponse({'status': 'Exceeded Limit.'})
                return JsonResponse({'status': 'ok.'})

            except:
                return JsonResponse({'status': 'Exception error.'})
        return JsonResponse({'status': 'Request error.'})

    @method_decorator(login_required)
    def delete(self, request):
        req = literal_eval(request.body.decode('utf-8'))
        number_id = str(req['numberId'])
        if number_id:
            try:
                Number.objects.filter(
                    profile=self.request.user.profile,
                    id=number_id).delete()
                return JsonResponse({'status': 'ok.'})
            except:
                return JsonResponse({'status': 'Exception error.'})
        return JsonResponse({'status': 'Request error.'})


class PasswordsTemplateView(TemplateView):
    template_name = 'gerador/passwords.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if (self.request.user.is_authenticated):
            context['passwords'] = Password.objects.filter(
                profile=self.request.user.profile)

        context["page"] = 'gerador'
        context["section"] = 'senhas'
        return context

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    @method_decorator(login_required)
    def post(self, request):
        req = literal_eval((request.POST.get('json')))

        data = {
            'profile': self.request.user.profile,
            'password': req['password'],
        }
        savedPassword_form = PasswordForm(data=data)

        if savedPassword_form.is_valid():
            clean_savedPassword = savedPassword_form.clean()
            try:
                new_savedPassword = Password(
                    profile=clean_savedPassword['profile'],
                    password=clean_savedPassword['password'],
                )

                try:
                    new_savedPassword.save()
                except ValidationError:
                    return JsonResponse({'status': 'Exceeded Limit.'})
                return JsonResponse({'status': 'ok.'})
            except:
                return JsonResponse({'status': 'Exception error.'})
        return JsonResponse({'status': 'Request error.'})

    @method_decorator(login_required)
    def delete(self, request):
        req = literal_eval(request.body.decode('utf-8'))
        password_id = str(req['passwordId'])

        if password_id:
            try:
                Password.objects.filter(
                    profile=self.request.user.profile,
                    id=password_id).delete()
                return JsonResponse({'status': 'ok.'})
            except:
                return JsonResponse({'status': 'Exception error.'})
        return JsonResponse({'status': 'Request error.'})
