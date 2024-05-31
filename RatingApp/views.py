from django.shortcuts import render,redirect
from .models import RatingTableOne,RatingTableTwo
from .forms import RatingTableOneForm,RatingTableTwoForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def Start_view(request):
    return render(request,'RatingApp/start.html')

def RatingTableOne_View(request):
    form = RatingTableOneForm()
    if request.method == 'POST':
        form = RatingTableOneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/ratingtwo')
    return render(request,'RatingApp/rating.html',{'data':form})


def RatingTableTwo_View(request):
    form = RatingTableTwoForm()
    if request.method == 'POST':
        form = RatingTableTwoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/success')
    return render(request,'RatingApp/rating.html',{'data':form})


def Success_view(request):
    return render(request,'RatingApp/success.html')

@login_required(login_url='/admin')
def Result_view(request):
    Rating1_details=RatingTableOne.objects.all()
    Rating2_details=RatingTableTwo.objects.all()
    return render(request,'RatingApp/result.html',{'data_1':Rating1_details,'data_2':Rating2_details})


    