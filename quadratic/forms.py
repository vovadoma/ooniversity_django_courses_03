# coding: utf-8

from django import forms

class QuadraticForm(forms.Form):
    a = forms.IntegerField(label=u"коэффициент a")
    b = forms.IntegerField(label=u"коэффициент b")
    c = forms.IntegerField(label=u"коэффициент c")

    def clean_a(self):
        if self.cleaned_data['a'] == 0:
            raise forms.ValidationError(u"коэффициент при первом слагаемом уравнения не может быть равным нулю")
        return self.cleaned_data['a']