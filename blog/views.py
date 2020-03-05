#imports to SOAP client zeep

from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Post
from django.views import View

import os
from django.conf import settings
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from xhtml2pdf import pisa

# Create your views here.

def notification(request):
    template = 'blog/notification.html'

    investor = 'ALFREDO REYES CORTES'
    address = 'NOGALES 108, COL. PRIMAVERA'
    city = 'OAXACA DE JUAREZ, OAXACA'
    zip_code = '68140'
    investment_amount = '$20,000.00'
    amount_twelve = 'NOTHING'
    amount_eighteen = 'NOTHING'
    amount_twenty = 'NOTHING' 
    data_dict = {'investor':investor,'address':address,'city':city,'zip_code':zip_code,
    'investment_amount': investment_amount, 'amount_twelve': amount_twelve,
    'amount_eighteen': amount_eighteen, 'amount_twenty': amount_twenty
    }
    
    return render(request, template, data_dict)

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

#all about xhtml2pdf
def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    # use short variable names
    sUrl = settings.STATIC_URL      # Typically /static/
    sRoot = settings.STATIC_ROOT    # Typically /home/userX/project_static/
    mUrl = settings.MEDIA_URL       # Typically /static/media/
    mRoot = settings.MEDIA_ROOT     # Typically /home15/userX/project_static/media/

    # convert URIs to absolute system paths
    if uri.startswith(mUrl):
        path = os.path.join(mRoot, uri.replace(mUrl, ""))
    elif uri.startswith(sUrl):
        path = os.path.join(sRoot, uri.replace(sUrl, ""))
    else:
        return uri  # handle absolute uri (ie: http://some.tld/foo.png)

    # make sure that file exists
    if not os.path.isfile(path):
            raise Exception(
                'media URI must start with %s or %s' % (sUrl, mUrl)
            )
    return path

def render_pdf_view(request):
    template_path = 'blog/index.html'
   
    dict = {'name': 'alfredo', 'operation':'STP', 'concept':'Pago', 'amount':'8000.00',
    'issuing_bank':'STP', 'receiving_bank':'Bancomer', 'datetime':'13/Abr/2019 08:10',
    'reference':'SKU41346', 'tracking_key':'6451542'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Comprobante_de_pago.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(dict)

    # create a pdf
    pisaStatus = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)
    # if error then show some funy view
    if pisaStatus.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response