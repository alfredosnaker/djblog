from django.urls import path

from . import views 

#app_name = 'blog'

urlpatterns = [
    path('', views.notification, name='notification'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),  
    path('conver_to_pdf/', views.render_pdf_view, name='render_pdf_view')
]
