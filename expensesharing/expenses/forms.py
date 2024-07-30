from django import forms
from .models import User, Expense, ExpenseSplit

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'name', 'mobile_number']

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['description', 'total_amount', 'split_method']

class ExpenseSplitForm(forms.ModelForm):
    class Meta:
        model = ExpenseSplit
        fields = ['user', 'amount', 'percentage']
