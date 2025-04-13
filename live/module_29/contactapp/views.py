from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import FilterSet,  NumberFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Contact, Author, Book
from .serializers import ContactSerializer, AuthorSerializer, BookSerializer

from rest_framework.pagination import PageNumberPagination
class MyPagination(PageNumberPagination):
    page_size = 2


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["author", "title"]   # disable if use filterset_class
    # filterset_class = BookFilter   # enable if use BookFilter class

    # filter_backends = [OrderingFilter]
    # ordering_fields = ["author", "title"]

    # filter_backends = [SearchFilter]   # for search (search and filter not work together)
    # search_fields = ["title"]

    #.............................Pagination
    pagination_class = MyPagination


# class BookFilter(FilterSet):    # filtaring book based on price
#     min_price = NumberFilter(field_name="price", lookup_expr="gte")
#     max_price = NumberFilter(field_name="price", lookup_expr="lte")

#     class Meta:
#         model = Book
#         fields = ["min_price", "max_price"]

