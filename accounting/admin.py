from django.contrib import admin
from .models import IncomeCategory,Income,ExpensesCategory,Expenses
# Register your models here.
admin.site.register(IncomeCategory)

admin.site.register(ExpensesCategory)

class IncomeAdmin(admin.ModelAdmin):
    list_display = ['title','rupes','category','date']
    list_filter = ['category','date']
    search_fields = ['title','date']



admin.site.register(Income,IncomeAdmin)


class ExpensesAdmin(admin.ModelAdmin):
    list_display = ['title','rupes','category','date']
    list_filter = ['category','date']
    search_fields = ['title','date']



admin.site.register(Expenses,ExpensesAdmin)