from django.urls import path
from api.views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    path('',getData)

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
