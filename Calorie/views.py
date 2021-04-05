from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *
from .filters import fooditemFilter

from django.views.generic.edit import  CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages


def home(request):
    breakfast=Category.objects.filter(name='breakfast')[0].fooditem_set.all()[:5]
    lunch=Category.objects.filter(name='lunch')[0].fooditem_set.all()[:5]
    dinner=Category.objects.filter(name='dinner')[0].fooditem_set.all()[:5]
    snacks=Category.objects.filter(name='snacks')[0].fooditem_set.all()[:5]
    customers=Customer.objects.all()
    context={'breakfast':breakfast,
              'lunch':lunch,
              'dinner':dinner,
              'snacks':snacks,
              'customers':customers,
            }
    return render(request,'main.html',context)


def userPage(request):
    user=request.user
    cust=user.customer
    fooditems=Fooditem.objects.filter()
    myfilter = fooditemFilter(request.GET,queryset=fooditems)
    fooditems=myfilter.qs
    total=UserFooditem.objects.all()
    myfooditems=total.filter(customer=cust)
    cnt=myfooditems.count()
    querysetFood=[]
    for food in myfooditems:
        querysetFood.append(food.fooditem.all())
    finalFoodItems=[]
    for items in querysetFood:
        for food_items in items:
            finalFoodItems.append(food_items)
    totalCalories=0
    for foods in finalFoodItems:
        totalCalories+=foods.calorie

    CalorieLeft=2000-totalCalories
    if totalCalories >= 2000:
        messages.warning(request, 'Your Calorie is Over Limit 2000.')
    context={'CalorieLeft':CalorieLeft,'totalCalories':totalCalories,'cnt':cnt,'foodlist':finalFoodItems,'fooditem':fooditems,'myfilter':myfilter}
    return render(request,'user.html',context)


def fooditem(request):
    breakfast=Category.objects.filter(name='breakfast')[0].fooditem_set.all()
    bcnt=breakfast.count()
    lunch=Category.objects.filter(name='lunch')[0].fooditem_set.all()
    lcnt=lunch.count()
    dinner=Category.objects.filter(name='dinner')[0].fooditem_set.all()
    dcnt=dinner.count()
    snacks=Category.objects.filter(name='snacks')[0].fooditem_set.all()
    scnt=snacks.count()
    context={'breakfast':breakfast,
              'bcnt':bcnt,
              'lcnt':lcnt,
              'scnt':scnt,
              'dcnt':dcnt,
              'lunch':lunch,
              'dinner':dinner,
              'snacks':snacks,
            }
    return render(request,'fooditem.html',context)


def createfooditem(request):
    form = fooditemForm()
    if request.method == 'POST':
        form = fooditemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fooditem')
    context={'form':form}
    return render(request,'createfooditem.html',context)


def addFooditem(request):
    user=request.user
    cust=user.customer
    if request.method=="POST":
        form =addUserFooditem(request.POST)
        if form.is_valid():
            userfooditem=form.save(commit=False)
            userfooditem.customer=cust
            userfooditem.save()
            form.save_m2m()
            return redirect('userPage')
    form=addUserFooditem()
    context={'form':form}
    return render(request,'addUserFooditem.html',context)


class ItemUpdate(LoginRequiredMixin, UpdateView):
  model = Fooditem
  fields = '__all__' 



def item_delete(request, pk):
  query = UserFooditem.objects.filter(fooditem=pk)
  query.delete()
  return HttpResponseRedirect(reverse('userPage'))

 


            




