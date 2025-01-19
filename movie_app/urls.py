from . import views
from django.urls import path

urlpatterns = [
    path('', views.directors_list_api_view),
    path('<int:id>/', views.review_detail_api_view),
    path('', views.review_list_api_view),
    path('<int:id>/', views.movie_detail_api_view),
    path('', views.movie_list_api_view)
]