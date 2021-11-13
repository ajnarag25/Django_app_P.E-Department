from django import forms
from .models import Registration, Buy, Reserve, Borrow

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'

class BuyForm(forms.ModelForm):
    class Meta:
        model = Buy
        fields = '__all__'

class ReserveForm(forms.ModelForm):
    class Meta:
        model = Reserve
        fields = '__all__'

class BorrowForm(forms.ModelForm):
    class Meta:
        model = Borrow
        fields = '__all__'