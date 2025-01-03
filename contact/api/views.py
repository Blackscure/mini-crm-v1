from rest_framework.permissions import IsAuthenticated
from contact.api.serializers import ContactSerializer
from contact.models import Contact
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from utils.paginator import CustomPaginator



class ContactListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            contacts = Contact.objects.all()
            paginator = CustomPaginator()
            paginated_contacts = paginator.paginate_queryset(contacts, request)
            serializer = ContactSerializer(paginated_contacts, many=True)
            return paginator.get_paginated_response(serializer.data)
        except Exception as e:
            return Response({
                'success': False,
                'message': f'An error occurred: {str(e)}',
                'data': []
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def post(self, request):
        try:
            serializer = ContactSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'success': True,
                    'message': 'Contact created successfully',
                    'data': serializer.data
                }, status=status.HTTP_201_CREATED)
            return Response({
                'success': False,
                'message': 'Validation errors occurred',
                'errors': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                'success': False,
                'message': f'An error occurred: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ContactDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Contact.objects.get(pk=pk)
        except Contact.DoesNotExist:
            return None

    def get(self, request, pk):
        contact = self.get_object(pk)
        if not contact:
            return Response({
                'success': False,
                'message': 'Contact not found'
            }, status=status.HTTP_404_NOT_FOUND)
        serializer = ContactSerializer(contact)
        return Response({
            'success': True,
            'message': 'Contact retrieved successfully',
            'data': serializer.data
        }, status=status.HTTP_200_OK)

    def put(self, request, pk):
        contact = self.get_object(pk)
        if not contact:
            return Response({
                'success': False,
                'message': 'Contact not found'
            }, status=status.HTTP_404_NOT_FOUND)
        serializer = ContactSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True,
                'message': 'Contact updated successfully',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        return Response({
            'success': False,
            'message': 'Validation errors occurred',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        contact = self.get_object(pk)
        if not contact:
            return Response({
                'success': False,
                'message': 'Contact not found'
            }, status=status.HTTP_404_NOT_FOUND)
        serializer = ContactSerializer(contact, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True,
                'message': 'Contact partially updated successfully',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        return Response({
            'success': False,
            'message': 'Validation errors occurred',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        contact = self.get_object(pk)
        if not contact:
            return Response({
                'success': False,
                'message': 'Contact not found'
            }, status=status.HTTP_404_NOT_FOUND)
        contact.delete()
        return Response({
            'success': True,
            'message': 'Contact deleted successfully'
        }, status=status.HTTP_204_NO_CONTENT)
