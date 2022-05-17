from django.views.generic import TemplateView

from pytz import common_timezones as ctz
from pytz import timezone
from datetime import datetime, timedelta

from copy import deepcopy

class RelogioTemplateView(TemplateView):
    template_name = 'tempo/time.html'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def float_to_hours(self, num):
        sign = 1 if (num >= 0) else -1    	
        num = abs(num)
        hours = str(timedelta(hours=num))[:-3]

        if (sign == -1):
            hours = '-' + str(hours)
        else:
            hours = '+' + str(hours)
    	
        return hours

    def get_timezones(self):
        tz_list = []
        tzs = deepcopy(ctz)
        tzs.remove('UTC')
        tzs.remove('GMT')
        for t in tzs:
            tz_list.append({
                'timezone': t,
                'UTCoffset': self.float_to_hours(datetime.now(timezone(t)).utcoffset().total_seconds()/3600),
            })
        return tz_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = 'tempo'
        context["section"] = 'relogio'
        context["timezones"] = self.get_timezones()
        return context

class CronometroTemplateView(TemplateView):
    template_name = 'tempo/stopwatch.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = 'tempo'
        context["section"] = 'cronometro'
        return context


class TemporizadorTemplateView(TemplateView):
    template_name = 'tempo/timer.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)    

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = 'tempo'
        context["section"] = 'temporizador'
        return context


