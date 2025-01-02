from rest_framework.permissions import IsAuthenticated
from lead.api.serializers import LeadSerializer
from lead.models import Lead
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from utils.paginator import CustomPaginator

class LeadListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            leads = Lead.objects.all()
            paginator = CustomPaginator()
            paginated_leads = paginator.paginate_queryset(leads, request)

            if paginated_leads:
                serializer = LeadSerializer(paginated_leads, many=True)
                return paginator.get_paginated_response({
                    'success': True,
                    'message': 'Leads retrieved successfully',
                    'count': leads.count(),
                    'data': serializer.data
                })
            else:
                return Response({
                    'success': True,
                    'message': 'No leads found',
                    'count': 0,
                    'data': []
                }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                'success': False,
                'message': f'An error occurred: {str(e)}',
                'data': []
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
            try:
                serializer = LeadSerializer(data=request.data, context={'request': request})
                if serializer.is_valid():
                    serializer.save(created_by=request.user)
                    return Response({
                        'success': True,
                        'message': 'Lead created successfully',
                        'data': serializer.data
                    }, status=status.HTTP_201_CREATED)

                return Response({
                    'success': False,
                    'message': 'Validation failed',
                    'errors': serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)

            except Exception as e:
                return Response({
                    'success': False,
                    'message': 'An error occurred while creating the lead',
                    'error': str(e)
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LeadDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Lead.objects.get(pk=pk)
        except Lead.DoesNotExist:
            return None
        except Exception as e:
            return {'error': f'An error occurred while fetching the lead: {str(e)}'}

    def get(self, request, pk):
        try:
            lead = self.get_object(pk)
            if isinstance(lead, dict):  
                return Response({
                    'success': False,
                    'message': lead['error'],
                    'data': []
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            if lead is None:
                return Response({'error': 'Lead not found'}, status=status.HTTP_404_NOT_FOUND)

            serializer = LeadSerializer(lead)
            return Response({
                'success': True,
                'message': 'Lead retrieved successfully',
                'data': serializer.data
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                'success': False,
                'message': f'An error occurred: {str(e)}',
                'data': []
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            lead = self.get_object(pk)
            if isinstance(lead, dict):  
                return Response({
                    'success': False,
                    'message': lead['error'],
                    'data': []
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            if lead is None:
                return Response({'error': 'Lead not found'}, status=status.HTTP_404_NOT_FOUND)

            serializer = LeadSerializer(lead, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'success': True,
                    'message': 'Lead updated successfully',
                    'data': serializer.data
                }, status=status.HTTP_200_OK)
            return Response({
                'success': False,
                'message': 'Invalid data',
                'errors': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({
                'success': False,
                'message': f'An error occurred: {str(e)}',
                'data': []
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, pk):
        try:
            lead = self.get_object(pk)
            if isinstance(lead, dict):  
                return Response({
                    'success': False,
                    'message': lead['error'],
                    'data': []
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            if lead is None:
                return Response({'error': 'Lead not found'}, status=status.HTTP_404_NOT_FOUND)

            serializer = LeadSerializer(lead, data=request.data, partial=True, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'success': True,
                    'message': 'Lead partially updated successfully',
                    'data': serializer.data
                }, status=status.HTTP_200_OK)
            return Response({
                'success': False,
                'message': 'Invalid data',
                'errors': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({
                'success': False,
                'message': f'An error occurred: {str(e)}',
                'data': []
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            lead = self.get_object(pk)
            if isinstance(lead, dict):  
                return Response({
                    'success': False,
                    'message': lead['error'],
                    'data': []
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            if lead is None:
                return Response({'error': 'Lead not found'}, status=status.HTTP_404_NOT_FOUND)

            lead.delete()
            return Response({
                'success': True,
                'message': 'Lead deleted successfully',
                'data': []
            }, status=status.HTTP_204_NO_CONTENT)

        except Exception as e:
            return Response({
                'success': False,
                'message': f'An error occurred: {str(e)}',
                'data': []
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)