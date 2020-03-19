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

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def main_page(request):
    url = 'https://business.goldenclickads.com/login/'
    content = 'Le damos la bienvenida a Golden Click Ads.'
    person = 'soniaRam78'
    razon_to_redirect = 'Para continuar con la activacion visite el siguiente enlace:'
    affair = 'ACTIVACION DE SU CUENTA'
    url_help = 'https:www.google.com/imghp'
    data = {
        'affair': affair,
        'content': content,
        'person': person, 
        'razon_to_redirect': razon_to_redirect,
        'url': url,
        'url_help': url_help
    }

    page = 'blog/notify.html'
    return render(request, page, data)

def send_email(request):
    sender_email = "mailto:business@goldenclickads.com"
    receiver_email = "sistemas@selectaglobal.com"
    password = input("Type your password and press enter:")

    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = sender_email
    message["To"] = receiver_email
    text = """
        Hi,
        How are you?
        Real Python has many great tutorials:
        www.realpython.com
    """

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

    template_path = 'blog/notification.html'
    template = get_template(template_path)
    html = template.render(data_dict)

    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)
    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )

    return render(request,'blog/notification.html', data_dict)
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


def ws_recive_document(request):

    if request.POST:
        keywords = request.POST.get('id_keywords', False)
        print(keywords)
    return render(request,'blog/index.html')


def ws_download_document(request):
    path = "main/static/xlsx/Empleados.xlsx"
    file_path  = os.path.join(os.path.abspath(''), path)
    excel_name = os.path.basename(file_path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(
                fh, 
                content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            )
            response['Content-Disposition'] = f'attachment; filename={excel_name}'
            return response
    raise Http404