from functools import partial
from django.shortcuts import get_object_or_404


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import SongSerializer
from .models import Song

@api_view(['GET', 'POST'])
def song_list(request):
   
    if request.method == 'GET':
        song = Song.objects.all()
        serializer = SongSerializer(song,many=True)
        return Response(serializer.data)



    elif request.method == 'POST':
            serializer = SongSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    

@api_view(['GET','PUT', 'DELETE','PATCH'])                
def song_detail(request, pk):
    song = get_object_or_404(Song, pk=pk)
    if request.method == 'GET':
            serializer = SongSerializer(song);
            return Response(serializer.data)
    elif request.method == 'PUT':
            serializer = SongSerializer(song, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
            song.delete()
            return Response(status.HTTP_204_NO_CONTENT)
    elif request.method =='PATCH':
        song.likes += 1 
        serializer = SongSerializer(song, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data)
        
        
    # elif PATCH
    # line 31 holds are song object in song variable 
    # we need to take song.likes =+ 1 
    # then we want pass this into the serializer and save 


    