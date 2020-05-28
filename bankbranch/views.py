from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from . serializers import BranchSearchSerializer
from . models import BankBranch

class BranchSearchView(viewsets.ModelViewSet):
	queryset = BankBranch.objects.all()
	serializer_class = BranchSearchSerializer

