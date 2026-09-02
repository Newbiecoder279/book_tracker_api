from django.urls import path
from . import views
urlpatterns = [
    path('books/',views.book_view.as_view(), name="books"),
    path('books/<int:pk>/',views.book_details.as_view(), name="books_details"),    
]
