from django.urls import path
from lead.api.views import LeadDetailAPIView, LeadListCreateAPIView


urlpatterns = [
    path('leads/', LeadListCreateAPIView.as_view(), name='lead-list-create'),
    path('leads/<int:pk>/', LeadDetailAPIView.as_view(), name='lead-detail'),
]
