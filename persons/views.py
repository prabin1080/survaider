import time
from django.db.models import Count
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from .models import Person
from .serializers import PersonSerializer, RelationshipGraphSerializer, SexGraphSerializer


class PersonListAPIView(ListAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        sex = self.request.query_params.get('sex', None)
        race = self.request.query_params.get('race', None)
        relationship = self.request.query_params.get('relationship', None)
        if sex:
            queryset = queryset.filter(sex=sex)
        if race:
            queryset = queryset.filter(race=race)
        if relationship:
            queryset = queryset.filter(relationship=relationship)
        return queryset

    @method_decorator(cache_page(60*60*2))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class RelationshipGraph(ListAPIView):
    queryset = Person.objects.all()

    @method_decorator(cache_page(60*60*2))
    def list(self, request, *args, **kwargs):
        queryset = Person.objects.values('relationship').order_by('relationship').annotate(count=Count('relationship'))
        serializer = RelationshipGraphSerializer(queryset, many=True)
        return Response(serializer.data)


class SexGraph(ListAPIView):
    queryset = Person.objects.all()

    @method_decorator(cache_page(60*60*2))
    def list(self, request, *args, **kwargs):
        queryset = Person.objects.values('sex').order_by('sex').annotate(count=Count('sex'))
        serializer = SexGraphSerializer(queryset, many=True)
        return Response(serializer.data)