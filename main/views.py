from django.shortcuts import render,redirect
from .models import *
from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def HomePage(r):
	if r.method == 'POST':
		title=r.POST.get('title')
		date=r.POST.get("date")
		ToDoList.objects.create(title=title,date=date,checked=False)

	DATA = {
		"tasks":ToDoList.objects.all().order_by('-id'),
		'today':str(datetime.today().date()),
	}
	return render(r,"home.html",DATA)

def ChangePage(r,pk):
	task = ToDoList.objects.get(id=pk)
	if task.checked == False:
		task.checked = True
		task.save()
	elif task.checked == True:
		task.checked = False
		task.save()

	return redirect("home")

def DeletePage(r,pk):
	target_task = ToDoList.objects.get(id=pk)
	target_task.delete()
	# print(r.path)
	return redirect('home')

def PathPage(r):
	if r.method == 'POST':
		value = r.POST.get('status')
		if value == '1':
			return redirect('home')
		elif value == '2':
			return redirect("completed")
		elif value == '3':
			return redirect("active")

	return redirect('home')

def CompletedPage(r):
	DATA = {
		"tasks":ToDoList.objects.filter(checked=True),
	}
	return render(r,"home.html",DATA)

def ActivePage(r):
	DATA = {
		"tasks":ToDoList.objects.filter(checked=False),
	}
	return render(r,"home.html",DATA)

def ChangeTaskPage(r):
	if r.method == 'POST':
		title=r.POST.get("new-title")
		date=r.POST.get("new-date")
		task_id = r.POST.get("id")
		target_task = ToDoList.objects.get(id=task_id)
		target_task.title = title
		target_task.date = date
		target_task.save()
		return redirect("home")