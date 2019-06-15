from django.shortcuts import render
from django.http import HttpResponse
from .models import Board

# Create your views here.
def home(request):
	boards = Board.objects.all()
	return render(request,'fancyhome.html',{'boards':boards})
def board_topics(request,pk):
	baord = Baord.objects.get(pk=pk)
	return render(request, 'topics.html', {'board': board}