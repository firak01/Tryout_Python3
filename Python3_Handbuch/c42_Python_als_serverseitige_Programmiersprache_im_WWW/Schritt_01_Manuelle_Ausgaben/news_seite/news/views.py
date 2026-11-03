from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Meldung, Kommentar

def meldungen(request):
    zeilen = []
    for m in Meldung.objects.all():
        zeilen.append("Meldung: '{}' vom {}".format(
            m.titel, m.zeitstempel.strftime('%d.%m.%Y um %H:%M')))
        zeilen.append(f'Text: {m.text}'.format(m.text))
        zeilen += ['', '-' * 30, '']
    antwort = HttpResponse('\n'.join(zeilen))
    antwort['Content-Type'] = 'text/plain'
    return antwort

def meldungen_detail(request, meldungs_id):
    m = get_object_or_404(Meldung, id=meldungs_id)
    zeilen = [
        "Titel: '{}' vom {}".format(
            m.titel, m.zeitstempel.strftime('%d.%m.%Y um %H:%M')),
        f'Text: {m.text}'.format(m.text),
        '', '-' * 30,
        'Kommentare:', '']
    zeilen += [f'{k.autor}: {k.text}'.format(k.autor, k.text) 
               for k in m.kommentar_set.all()]
    antwort = HttpResponse('\n'.join(zeilen))
    antwort['Content-Type'] = 'text/plain'
    return antwort
