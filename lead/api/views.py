from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Lead
from .serializers import LeadSerializer

class LeadListCreateAPIView(APIView):
    """
    Handle GET and POST requests for leads.
    """
    def get(self, request):
        leads = Lead.objects.all()
        serializer = LeadSerializer(leads, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = LeadSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(created_by=request.user)  # Assuming user is authenticated
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LeadDetailAPIView(APIView):
    """
    Handle GET, PUT, PATCH, and DELETE requests for a single lead.
    """
    def get_object(self, pk):
        try:
            return Lead.objects.get(pk=pk)
        except Lead.DoesNotExist:
            return None

    def get(self, request, pk):
        lead = self.get_object(pk)
        if lead is None:
            return Response({'error': 'Lead not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = LeadSerializer(lead)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        lead = self.get_object(pk)
        if lead is None:
            return Response({'error': 'Lead not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = LeadSerializer(lead, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        lead = self.get_object(pk)
        if lead is None:
            return Response({'error': 'Lead not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = LeadSerializer(lead, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        lead = self.get_object(pk)
        if lead is None:
            return Response({'error': 'Lead not found'}, status=status.HTTP_404_NOT_FOUND)
        lead.delete()
        return Response({'message': 'Lead deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
