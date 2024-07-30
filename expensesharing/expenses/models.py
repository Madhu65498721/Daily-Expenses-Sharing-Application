from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Expense(models.Model):
    EQUAL = 'Equal'
    EXACT = 'Exact'
    PERCENTAGE = 'Percentage'

    SPLIT_METHODS = [
        (EQUAL, 'Equal'),
        (EXACT, 'Exact'),
        (PERCENTAGE, 'Percentage'),
    ]

    description = models.CharField(max_length=255)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    split_method = models.CharField(max_length=10, choices=SPLIT_METHODS)
    users = models.ManyToManyField(User, through='ExpenseSplit')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description

class ExpenseSplit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

class BalanceSheet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_expenses = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.user.name}'s Balance Sheet"
