from django.urls import path

from products import views

urlpatterns = [

    path('all/', views.ProductsList.as_view()),
    path('product/<int:pk>/', views.ProductDetail.as_view()),
]
