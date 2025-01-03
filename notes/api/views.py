from rest_framework.permissions import IsAuthenticated
from notes.models import Note
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import NoteSerializer

class NoteListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            notes = Note.objects.all()
            if notes.exists():
                serializer = NoteSerializer(notes, many=True)
                return Response({
                    'success': True,
                    'message': 'Notes retrieved successfully',
                    'data': serializer.data
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    'success': True,
                    'message': 'No notes found',
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
            serializer = NoteSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'success': True,
                    'message': 'Note created successfully',
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

class NoteDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Note.objects.get(pk=pk)
        except Note.DoesNotExist:
            return None

    def get(self, request, pk):
        note = self.get_object(pk)
        if note is None:
            return Response({'success': False, 'message': 'Note not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = NoteSerializer(note)
        return Response({'success': True, 'message': 'Note retrieved successfully', 'data': serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, pk):
        note = self.get_object(pk)
        if note is None:
            return Response({'success': False, 'message': 'Note not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = NoteSerializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'message': 'Note updated successfully', 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'success': False, 'message': 'Validation errors occurred', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        note = self.get_object(pk)
        if note is None:
            return Response({'success': False, 'message': 'Note not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = NoteSerializer(note, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'message': 'Note updated successfully', 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'success': False, 'message': 'Validation errors occurred', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        note = self.get_object(pk)
        if note is None:
            return Response({'success': False, 'message': 'Note not found'}, status=status.HTTP_404_NOT_FOUND)
        note.delete()
        return Response({'success': True, 'message': 'Note deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
