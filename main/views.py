from django.shortcuts import render
from rest_framework.generics import ListAPIView
from django.db.models import Q 

from .models import Table
from .filters import TableFilter
from .serializers import TableSerializer


class TableListView(ListAPIView):
	queryset = Table.objects.all()
	serializer_class = TableSerializer
	filter_class = TableFilter

	def get_queryset(self):
		tb = self.filter_class(self.request.GET, super().get_queryset())
		return tb.qs