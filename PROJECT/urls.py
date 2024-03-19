from django.conf import settings
from django.conf.urls.static import static
from mainApp.views import *
from userApp.views import LoginView

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('user/', include('userApp.urls')),
                  path('main/', include('mainApp.urls')),
                  path('order/', include('orderApp.urls')),

                  path('', Home.as_view(), name='home'),

                  path('', LoginView.as_view(), name='login')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
