from django.contrib import admin
from django.urls import path, include
from movie_app import views
from . import swagger

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/movie_app/', include('movie_app.urls')),
    path('api/v1/movie_app/', include('users.urls')),
    # path('api/v1/directors/', views.directors_list_api_view),
    # path('api/v1/movies/', views.movie_list_api_view),
    # path('api/v1/reviews/', views.review_list_api_view),
    # path('api/v1/directors/<int:id>/', views.director_detail_api_view),
    # path('api/v1/movies/<int:id>/', views.movie_detail_api_view),
    # path('api/v1/reviews/<int:id>/', views.review_detail_api_view),
    # path('api/v1/movies/reviews/', views.average_rating_api_view),
]

urlpatterns += swagger.urlpatterns
