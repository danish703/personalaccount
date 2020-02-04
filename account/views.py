from django.shortcuts import render,redirect
from accounting.models import Income,Expenses
import datetime
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.db.models.aggregates import Sum

@login_required(login_url='/admin/login')
def dashboard(request):
    context = {
        'income':Income.objects.all()[::-1][:10],
        'expenses': Expenses.objects.all()[::-1][:10],
        'month_expenses_total':getCurrentMonthExpenses(),
        'year_expenses_total': getCurrentMonthExpenses(),
        'month_income_total': getCurrentMonthIncome(),
        'year_income_total': getCurrentMonthIncome(),
        'month_saving':getCurrentMonthIncome()-getCurrentMonthExpenses(),
        'year_saving':getCurrentYearIncome()-getCurrentYearExpenses(),
    }
    return render(request,'dashboard.html',context)


def auth_logout(request):
    logout(request)
    return redirect('dashboard');


def getCurrentMonthExpenses():
    total = Expenses.objects.filter(date__month=getCurrentMonth(),date__year=getCurrentYear()).aggregate(Sum('rupes'))
    if total['rupes__sum'] is None:
        return 0;
    return total['rupes__sum']

def getCurrentYearExpenses():
    total = Expenses.objects.filter(date__year=getCurrentYear()).aggregate(Sum('rupes'))
    if total['rupes__sum'] is None:
        return 0;
    return total['rupes__sum']

def getCurrentMonthIncome():
    total = Income.objects.filter(date__month=getCurrentMonth(),date__year=getCurrentYear()).aggregate(Sum('rupes'))
    if total['rupes__sum'] is None:
        return 0;
    return total['rupes__sum']

def getCurrentYearIncome():
    total = Income.objects.filter(date__year=getCurrentYear()).aggregate(Sum('rupes'))
    if total['rupes__sum'] is None:
        return 0;
    return total['rupes__sum']


def getCurrentMonth():
    return datetime.date.today().month

def getCurrentYear():
    return datetime.date.today().year