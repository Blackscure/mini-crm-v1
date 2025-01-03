from django.urls import path

from contact.api.views import ContactDetailAPIView, ContactListCreateAPIView


urlpatterns = [
    path('contacts/', ContactListCreateAPIView.as_view(), name='contact-list-create'),
    path('contacts/<int:pk>/', ContactDetailAPIView.as_view(), name='contact-detail'),
]
