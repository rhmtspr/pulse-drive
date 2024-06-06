from django import forms
from .models import Car, Transaction

# class TransactionForm(forms.ModelForm):

#     class Meta:
#         model = Transaction
#         fields = ["rental_price", "rental_start_date", "rental_end_date"]
#         widgets = {
#             "rental_start_date": forms.SelectDateWidget(attrs={
#                 "class": "shadow appearance-none rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline",
#             }),
#             "rental_end_date": forms.SelectDateWidget(attrs={
#                 "class": "shadow appearance-none rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline",
#             }),
#             "rental_price": forms.NumberInput(attrs={
#                 "readonly": True
#             }),
#         }
