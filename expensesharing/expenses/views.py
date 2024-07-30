from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import User, Expense, ExpenseSplit, BalanceSheet
from .forms import UserForm, ExpenseForm, ExpenseSplitForm
import csv
from django.shortcuts import render

def home(request):
    return render(request, 'expenses/home.html')

def create_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'expenses/user_form.html', {'form': form})

def user_list(request):
    users = User.objects.all()
    return render(request, 'expenses/user_list.html', {'users': users})

def add_expense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save()
            return redirect('expense_detail', pk=expense.pk)
    else:
        form = ExpenseForm()
    return render(request, 'expenses/expense_form.html', {'form': form})

def expense_detail(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == "POST":
        form = ExpenseSplitForm(request.POST)
        if form.is_valid():
            split = form.save(commit=False)
            split.expense = expense
            split.save()
            return redirect('expense_detail', pk=expense.pk)
    else:
        form = ExpenseSplitForm()
    return render(request, 'expenses/expense_detail.html', {'expense': expense, 'form': form})

def download_balance_sheet(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="balance_sheet.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['User', 'Total Expenses'])
    
    for balance_sheet in BalanceSheet.objects.all():
        writer.writerow([balance_sheet.user.name, balance_sheet.total_expenses])
    
    return response
