from django.contrib import admin
from django.urls import path
from LearnAJAX import views as a
from quiz import views
from django.conf import settings
from django.conf.urls.static import static
        
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',welcome),
    path('quiz/',index),
    path('save_ans/',save_ans,name="saveans"),
    path('result/',result,name="result"),
        ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)