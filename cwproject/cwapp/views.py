from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Book
import datetime

def index(request):
    return HttpResponse("Read More Books, Not screens")


def addBook(request):
    book1 = Book(name='Charlie and The Chocolate Factory', pageNumber=4, genre='fiction', publishDate="1979-04-13")
    book1.save()
    book2 = Book(name='Cat in the Hat', pageNumber=7, genre='fiction', publishDate="2019-03-02")
    book2.save()
    return HttpResponse('New Book Added')


def all(request):
    booklist = Book.objects.all()
    for i in booklist:
        print(i.name)
    return HttpResponse("All Names Printed")

def allYear(request):
    booklist = Book.objects.all()
    for each in booklist:
        print(each.publishDate)
    if(each.publishDate >= datetime.date(2018,1,1)):
        print(each.name + " " + str(each.publishDate))
    return HttpResponse("All Dates Printed")
