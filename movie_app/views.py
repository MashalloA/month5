from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status


@api_view(['GET', 'PUT', 'DELETE'])
def director_detail_api_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        director.name = request.data.get('name')
        return Response(data=DirectorItemSerializer(director).data, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(http_method_names=['GET', 'POST'])
def directors_list_api_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        list_ = DirectorSerializer(instance=directors, many=True).data
        return Response(data=list_)
    elif request.method == 'POST':
        name = request.data.get('name')

        director = Director.objects.create(
            name=name,
        )
        return Response(data=DirectorItemSerializer(director).data, status=status.HTTP_201_CREATED)



@api_view(['GET'])
def movie_detail_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = DirectorSerializer(movie).data
    return Response(data=data)


@api_view(http_method_names=['GET'])
def movie_list_api_view(request):
    movies = Movie.objects.all()
    list_ = MovieSerializer(instance=movies, many=True).data
    return Response(data=list_)


@api_view(['GET'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = DirectorSerializer(review).data
    return Response(data=data)


@api_view(http_method_names=['GET'])
def review_list_api_view(request):
    reviews = Review.objects.all()
    list_ = ReviewSerializer(instance=reviews, many=True).data
    return Response(data=list_)
