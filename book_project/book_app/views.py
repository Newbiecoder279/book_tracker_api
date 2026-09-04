from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from django.db.models import Q 
from .pagination import BookPagination
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class book_view(generics.ListCreateAPIView):
    
    serializer_class = BookSerializer
    pagination_class = BookPagination
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = Book.objects.filter(
            owner = self.request.user
        )
        status = self.request.query_params.get('status')
        search = self.request.query_params.get('search')
        author = self.request.query_params.get('author')

        #filter by status
        if status:
            queryset = queryset.filter(status=status)

        #for search
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search)|
                Q(author__icontains=search)
            )
        if author:
            queryset = queryset.filter(
                Q(author__icontains=author)
            )
            
        return queryset
    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)

    
        

class book_details(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        
        return Book.objects.filter(
        owner = self.request.user
        )
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
