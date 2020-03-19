import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "galvramon44@gmail.com"
receiver_email = "galvramon44@gmail.com"
password = input("Type your password and press enter:")

message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["From"] = sender_email
message["To"] = receiver_email

# Create the plain-text and HTML version of your message
text = """
Hi,
How are you?
Real Python has many great tutorials:
www.realpython.com"""
#html = '/home/alfredo/djblog/blog/templates/blog/notification.html'

html = """
{% load static %}
<div class="adM">
</div><div style="padding:10px 0;background-color:#f8f2e5;margin:0" bgcolor="#f4ead6">
    <table style="background-color:#fff;margin:20px auto 28px;max-width:842px;padding:0;border:solid 1px #f8f2e5; background-repeat:no-repeat;vertical-align:bottom;" width="100%" cellspacing="0" cellpadding="0" border="0" bgcolor="#ffffff" background="{% static '/img/opacity.png' %}">
        <tbody>
            <tr>
                <td>
                    <table width="100%" cellspacing="0" cellpadding="0" border="0" >
                        <tbody>
                            <tr>
                                <td style="padding:20px 56px" align="left">
                                    <a href="https://www.mercadopago.com.mx/" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://www.mercadopago.com.mx/&amp;source=gmail&amp;ust=1583440865579000&amp;usg=AFQjCNEdpj7GreD5J45vw1l3JRiZFAQlXA">
                                        <img alt="Golden Clicks Ads" src="{% static '/img/golden_logo.png' %}" class="CToWUd" width="200" height="149" border="0">
                                    </a>
                                </td>
                            </tr>
                            <tr>  
                                <td style="border-top:solid 2px #c99e3c;display:block;font-size:1px" width="100%" height="1">&nbsp;</td>
                            </tr>
                            <tr>
                                <td style="font-size:1px" height="48">&nbsp;</td>
                            </tr>
                        </tbody>
                    </table>
                    <table style="padding:0 20px;text-align:left;margin:0 auto;max-width:760px" width="100%" cellspacing="0" cellpadding="0" border="0">
                        <tbody>
                            <tr>
                                <td >
                                    <span style="font-family:Arial;font-size:12px;color:#333333;line-height:25px">{{ investor }}</span>
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    <span style="font-family:Arial;font-size:12px;color:#333333;line-height:25px">{{ address }}</span>
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    <span style="font-family:Arial;font-size:12px;color:#333333;line-height:25px">{{ city }}</span>
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    <span style="font-family:Arial;font-size:12px;color:#333333;line-height:25px">{{ zip_code }}</span>
                                </td>
                            </tr>
                            <tr>
                                <td style="font-size:1px" height="40"></td>
                            </tr>
                        </tbody>
                    </table>
                    <table style="padding:0 20px;text-align:center;margin:0 auto;max-width:760px" width="100%" cellspacing="0" cellpadding="0" border="0">
                        <tbody>
                            <tr>
                                <td style="padding-bottom:24px">
                                    <span style="font-family:Arial;font-size:16px;color:#333333;line-height:25px;"><strong style="white-space:nowrap">PROYECTO DE INVERSION</strong></span>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <table style="padding:0 20px;text-align:justify;margin:0 auto;max-width:760px" width="100%" cellspacing="0" cellpadding="0" border="0">
                        <tbody>
                            <tr>
                                <td style="padding-bottom:24px">
                                    <p style="font-family:Arial;font-size:12px;color:#333333;line-height:25px">ESTIMADO <strong style="white-space:nowrap"> {{ investor }}</strong>, UNA VEZ ANALIZADA SU SOLICITUD DE INVERSIÓN PARA CON NUESTRA EMPRESA, ES QUE POR MEDIO DEL PRESENTE GOLDEN CLICK ADS, S.A.P.I. DE C.V., LE DA LAS GRACIAS POR PENSAR EN NOSOTROS PARA PODER HACER CRECER SU CAPITAL, ESTO POR MEDIO DE NUESTRA OPERACIÓN DE MARKETING EN INTERNET, MEDIANTE LA CUAL USTED PODRA OBTENER HASTA UN 2.5% DE RENDIMIENTO MENSUAL.
                                        CONFORME A LOS DISTINTOS PLAZOS DE INVERSIÓN CON LOS QUE CUENTA LA EMPRESA, ES QUE A CONTINUACIÓN SE AGREGA UNA TABLA CON LOS POSIBLES RENDIMIENTOS QUE SE GENERARIAN CONFORME A LA SUMA DE CAPITAL QUE USTED DESEA INVERTIR:</p>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <table style="padding:0 20px;background-color:#fafafa;border:1px solid #c99e3c;border-radius:4px;margin:0 auto;max-width:700px" cellspacing="0" cellpadding="0" border="0">
                        <tbody>
                            <tr>
                                <th style="font-family:Arial;font-size:12px;color:#333333;text-align:center;padding:10px 8px 10px 0"><strong>MONTO DE LA INVERSION</strong> </th>
                                <th style="font-family:Arial;font-size:12px;color:#333333;text-align:center;padding:10px 8px 10px 0"><strong>MESES</strong></th>
                                <th style="font-family:Arial;font-size:12px;color:#333333;text-align:center;padding:10px 8px 10px 0"><strong>TOTAL</strong></th>

                            </tr>
                            <tr valign="middle">
                                <td rowspan='3' style="font-family:Arial;font-size:12px;color:#333333;text-align:center;padding:10px 8px 10px 0">{{ investment_amount }}</td>
                                <td style="font-family:Arial;font-size:12px;color:#333333;text-align:left;padding:10px 8px 10px 0">12 MESES</td>
                                <td style="font-family:Arial;font-size:12px;color:#333333;text-align:left;padding:10px 8px 10px 0"><strong>{{ amount_twelve }}</strong></td>
                            </tr>
                            <tr valign="middle">
                                <td style="font-family:Arial;font-size:12px;color:#333333;text-align:left;border-top:1px solid #e9e9e9;padding:10px 8px 10px 0">18 MESES</td>
                                <td style="font-family:Arial;font-size:12px;color:#333333;text-align:left;border-top:1px solid #e9e9e9;padding:10px 8px 10px 0"><strong>{{ amount_eighteen }}</strong></td>
                            </tr>
                            <tr valign="middle">
                                <td style="font-family:Arial;font-size:12px;color:#333333;border-top:1px solid #e9e9e9;padding:10px 0 10px 8px;text-align:left">24 MESES</td>
                                <td style="font-family:Arial;font-size:12px;color:#333333;border-top:1px solid #e9e9e9;padding:10px 0 10px 8px;text-align:left"><strong>{{ amount_twenty }}</strong></td>
                            </tr>
                        </tbody>
                    </table>
                    <table style="padding:15px 0;text-align:justify;margin:0 auto;max-width:760px" width="100%" cellspacing="0" cellpadding="0" border="0">
                        <tbody>
                            <tr>
                                <td style="padding:24px">
                                    <p style="font-family:Arial;font-size:12px;color:#333333;line-height:25px">ASIMISMO, SE HACE DE SU CONOCIMIENTO QUE EL RETORNO DE LA INVERSIÓN COMO EL DEL RENDIMIENTO DE ESTA SE LE HARA LLEGAR 30 DIAS NATURALES DESPUES DE HABER FINALIZADO EL PLAZO QUE HAYA ELEGIDO.</p>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <table style="padding:0 20px;text-align:center;margin:0 auto;max-width:760px" width="100%" cellspacing="0" cellpadding="0" border="0">
                        <tbody>
                            <tr>
                                <td style="padding-bottom:24px">
                                    <p style="font-family:Arial;font-size:12px;color:#333333;line-height:25px">GRACIAS POR CONFIAR EN NOSOTROS</p>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <table style="padding:0 20px;text-align:center;margin:0 auto;max-width:760px" width="100%" cellspacing="0" cellpadding="0" border="0">
                        <tbody>
                            <tr>
                                <td style="padding-bottom:24px">
                                    <p style="font-family:Arial;font-size:12px;color:#333333;line-height:25px">BIANI RIDXI SANTOS ANTONIO</p> 
                                    <p style="font-family:Arial;font-size:12px;color:#333333;line-height:25px">
                                        ADMINISTRADORA UNICA DE GOLDEN CLICK ADS, S.A.P.I. DE C.V.
                                    </p>
                                </td>
                            </tr>
                        </tbody>
                    </table>
            </td>
        </tr>
    </tbody>
</table>

<table style="text-align:center;margin-bottom:28px" width="100%" cellspacing="0" cellpadding="0" border="0">
    <tbody><tr>
        <td style="padding:0"><span style="color:#999999;font-size:12px;font-family:Arial">Si tienes dudas, consulta nuestra <a href="https://www.mercadopago.com.mx/ayuda" style="text-decoration:none;font-family:Arial;color:#0637b3" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://www.mercadopago.com.mx/ayuda&amp;source=gmail&amp;ust=1583440865579000&amp;usg=AFQjCNGX4iZ8zLa4doqDojOtlSesdqh2Qw">ayuda</a>.</span></td>
    </tr>
</tbody></table>
</table>
</div></div><u></u>
<div class="adL">
</div>
"""

# Turn these into plain/html MIMEText objects
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