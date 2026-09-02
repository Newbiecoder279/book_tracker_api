from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from django.db.models import Q 
# Create your views here.

class book_view(generics.ListCreateAPIView):
    
    serializer_class = BookSerializer
    def get_queryset(self):
        queryset = Book.objects.all()
        status = self.request.query_params.get('status')
        search = self.request.query_params.get('search')
        author = self.request.query_params.get('author')

        if status:
            queryset = queryset.filter(status=status)
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
        
        

class book_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
