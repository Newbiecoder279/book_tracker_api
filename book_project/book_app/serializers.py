from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    def validate_title(self, value):
        if len(value.strip())<3:
            raise serializers.ValidationError(
                "Title must contain at least three letters."
            )
    def validate_author(self,value):
        if len(value.strip())<3:
            raise serializers.ValidationError(
                "Name of authors must be at least three letters."
            )
    def validate(self, data):
        if data['status'] == 'ongoing' and data['rating']>0:
            raise serializers.ValidationError(
                "Ongoing book cannot have a rating."
            )

    class Meta:
        model = Book
        fields = '__all__'