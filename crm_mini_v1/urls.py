from django.contrib import admin
from django.urls import path
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('apps/crm-mini/api/v1/authentication/', include('authentication.api.urls')),
    path('apps/crm-mini/api/v1/lead/', include('lead.api.urls')),
    path('apps/crm-mini/api/v1/contact/', include('contact.api.urls')),
]
