from django.shortcuts import render
from django.http import HttpResponse


def about(request):
	return HttpResponse('This is about page')


def home(request):
	return render(request, 'home.html')


def reverse(request):
	user_text = request.GET['usertext']
	split_text = user_text.split()
	leng = len(split_text)
	reversed_text = user_text[::-1]
	return render(request, 'reverse.html', {'usertext': user_text, 'leng': leng,
		'reversedtext': reversed_text})
