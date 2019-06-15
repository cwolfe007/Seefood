from django.shortcuts import render
from django.http import HttpResponse
from .models import Board

# Create your views here.
def home(request):
	boards = Board.objects.all()
	return render(request,'fancyhome.html',{'boards':boards})
def boards_topics(request,pk):
	board = Board.objects.get(pk=pk)
	return render(request, 'topics.html', {'board': board})