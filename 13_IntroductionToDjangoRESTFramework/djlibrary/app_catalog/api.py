from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from app_catalog.models import Author, Book
from app_catalog.serializers import AuthorSerializer, BookSerializer


class AuthorList(ListCreateAPIView):
    # queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get_queryset(self):
        queryset = Author.objects.all()
        first_name = self.request.query_params.get('first_name')
        if first_name:
            queryset = queryset.filter(first_name=first_name)
        return queryset


class AuthorDetail(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookList(ListCreateAPIView):
    # queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        if self.request.query_params:
            author = self.request.query_params.get('author')
            if author:
                if Author.objects.filter(last_name=author).exists():
                    book_author = Author.objects.get(last_name=author)
                    queryset = queryset.filter(author=book_author)
            title = self.request.query_params.get('title')
            if title:
                queryset = queryset.filter(title=title)
            number_of_pages = self.request.query_params.get('number_of_pages')
            if number_of_pages:
                queryset = queryset.filter(number_of_pages=number_of_pages)

        return queryset




class BookDetail(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
