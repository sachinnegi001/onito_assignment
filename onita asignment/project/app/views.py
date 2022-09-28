from django.shortcuts import render
from rest_framework import status

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response

from app.models import movies,ratings
from app.serializers import MoviesSerializer
from app.serializers import RatingsSerializer
from app.serializers import FileUploadSerializer
import io, csv, pandas as pd



#upload movies.csv file in the database by api------------------------------------
class UploadFileViewtomovies(generics.CreateAPIView):
    serializer_class = FileUploadSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        reader = pd.read_csv(file)
        for _, row in reader.iterrows():
            new_file = movies(
                       tconts = row['tconst'],
                       titleType= row["titleType"],
                       primaryTitle= row['primaryTitle'],
                       runtimeMinutes= row["runtimeMinutes"],
                       genres= row["genres"]
                       )
            new_file.save()
        return Response({"status": "success"},
                        status.HTTP_201_CREATED)
    
    
#upload ratings.csv by api in database----------------------------------
class UploadFileViewtoratings(generics.CreateAPIView):
    serializer_class = FileUploadSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        reader = pd.read_csv(file)
        for _, row in reader.iterrows():
            new_file = ratings(
                       tconst = row['tconst'],
                       averageRating= row["averageRating"],
                       numVotes= row['numVotes'],
                      )
            new_file.save()
        return Response({"status": "success"},
                        status.HTTP_201_CREATED)




    
#get movies ----------------------------------------
class movielist (APIView):
    def get(self,request):
        moviess=movies.objects.all().order_by("-runtimeMinutes")[:10]  #make descending order of our runtime minute field and take first 10 records
        serializer=MoviesSerializer(moviess,many=True)
       
        return Response(serializer.data)

    
    
    
  
 #get ratinga ----------------------------------------
class ratinglist (APIView):
    def get(self,request):
        Ratings=ratings.objects.all().order_by('-averageRating').filter(averageRating__gte=6.0)
        serializer=RatingsSerializer(Ratings,many=True)
        return Response(serializer.data)

    
    
    
#post request to add new movie-----------------------------
class Movielist (APIView):
    def post(self,request):
        serializer=MoviesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({"success"})
                       
      
# # Create your views here.
