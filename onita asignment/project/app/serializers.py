from rest_framework import serializers
from app.models import ratings,movies


class FileUploadSerializer(serializers.Serializer):   #to upload file 
    file = serializers.FileField()


class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model=movies
        fields = ['tconts', 'primaryTitle', 'runtimeMinutes','genres']
      
      
        
class RatingsSerializer(serializers.ModelSerializer):
    datta = MoviesSerializer(many=True ,read_only=True)
    class Meta:
        model=ratings
        fields = '__all__'
        
   
        
        
        
    
