from django import forms

class avgmarks(forms.Form):
    num1=forms.FloatField(label="Marks in Math")
    num2=forms.FloatField(label="Marks in Science")
    num3=forms.FloatField(label="Marks in English")
