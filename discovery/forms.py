from django import forms


class FormRegistration(forms.Form):                                                            
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Имя'}))                              
    second_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Фамилия'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Почта'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}))
