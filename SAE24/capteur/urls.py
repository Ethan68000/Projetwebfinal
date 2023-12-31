from . import views, donneeviews
from django.urls import path

urlpatterns = [
                path('ajout/', views.ajout),
                path('traitement/', views.traitement),
                path('index/', views.index),
                path("affiche/<str:id>/", views.affiche),
                path("update/<str:id>/", views.update),
                path("updatetraitement/<str:id>/", views.updatetraitement),
                path("delete/<str:id>/", views.delete),

                path('ajoutdon/', donneeviews.ajout),
                path('indexdon/', donneeviews.index),
    ]