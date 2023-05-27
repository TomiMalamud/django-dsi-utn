from django.shortcuts import render
from .models import Llamada
from django.views import generic

def index(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    llamadas = None

    if start_date and end_date:
        llamadas = Llamada.esDePeriodo(start_date, end_date)
    context = {
        'llamadas': llamadas,
    }
    return render(request, 'encuestas/index.html', context)


class DetailView(generic.DetailView):
    model = Llamada
    template_name = "encuestas/detail.html"