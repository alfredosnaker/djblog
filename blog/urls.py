from django.urls import path
from django.urls import include, path

from blog import views 

app_name = 'blog'

urlpatterns = [
    path('ws/', include([
        path ('recive-document', views.ws_recive_document, name='recive_document '),
        path ('donwload-document', views.ws_download_document, name='download_excel '),
    ])),
    path('other/', include([
        path('send-mail', views.main_page, name='main_page'),
        path('send-email/', views.send_email, name='send_email'),  
        path('post/<int:pk>/', views.post_detail, name='post_detail'),  
        path('conver_to_pdf/', views.render_pdf_view, name='render_pdf_view')
    ])),
]
