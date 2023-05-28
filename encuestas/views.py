from django.shortcuts import render, get_object_or_404
from .models import Llamada, Encuesta
import csv
from django.http import HttpResponse

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


def detail(request, pk):
    llamada_instance = get_object_or_404(Llamada, pk=pk)
    encuesta_instance = get_object_or_404(Encuesta, pk=pk)
      # Replace pk=1 with your desired filter criteria
    if 'export_csv' in request.GET:
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="llamada.csv"'

        # Create a CSV writer
        writer = csv.writer(response)
        writer.writerow(['Duration', 'Cliente', 'Estado'])

        # Write the llamada data to the CSV file
        writer.writerow([llamada_instance.duration, llamada_instance.cliente, llamada_instance.determinarUltimoEstado()])

        return response

    context = {
        'llamada': llamada_instance,
        'encuesta': encuesta_instance,
    }

    return render(request, 'encuestas/detail.html', context)



def some_view(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(
        content_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="somefilename.csv"'},
    )

    writer = csv.writer(response)
    writer.writerow(["First row", "Foo", "Bar", "Baz"])
    writer.writerow(["Second row", "A", "B", "C", '"Testing"', "Here's a quote"])

    return response