from django.contrib import admin
from .models import User, Expense, ExpenseSplit, BalanceSheet

admin.site.register(User)
admin.site.register(Expense)
admin.site.register(ExpenseSplit)
admin.site.register(BalanceSheet)
