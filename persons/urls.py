from django.urls import path

from .views import PersonListAPIView, RelationshipGraph, SexGraph

urlpatterns = [
    path('', PersonListAPIView.as_view()),
    path('relationship-graph/', RelationshipGraph.as_view()),
    path('sex-graph/', SexGraph.as_view()),
]
