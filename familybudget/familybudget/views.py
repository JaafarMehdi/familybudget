from django.contrib.auth.models import User
from rest_framework import viewsets

from .models.category import Category
from .models.entry import Entry
from .models.list import List
from .serializers.category_serializer import CategorySerializer
from .serializers.entry_serializer import EntrySerializer
from .serializers.list_serializer import ListSerializer
from .serializers.user_serializer import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    # todo add auth?
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# todo split into expenses and incomes
class EntryViewSet(viewsets.ModelViewSet):
    # todo add auth
    # todo add permissions
    # todo add category filters
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

class ListViewSet(viewsets.ModelViewSet):
    # todo add auth
    # todo add permissions
    queryset = List.objects.all()
    serializer_class = ListSerializer
