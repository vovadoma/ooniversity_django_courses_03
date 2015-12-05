# coding: utf-8
from django.shortcuts import render
from quadratic.forms import QuadraticForm
import math

def quadratic_results(request):

    a = b = c = ''
    msg = []
    disk = ''

    if request.GET:
        form = QuadraticForm(request.GET)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']

            ds = b * b - 4 * a * c
            disk = 'Дискриминант: %d' % ds

            if ds < 0:
                msg.append('Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.')
            elif ds == 0:
                x1 = (-b + math.sqrt(ds)) / (2 * a)
                msg.append('Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %.1f' % x1)
            else:
                x1 = (-b + math.sqrt(ds)) / (2 * a)
                x2 = (-b - math.sqrt(ds)) / (2 * a)
                msg.append('Квадратное уравнение имеет два действительных корня: x1 = %.1f, x2 = %.1f' % (x1, x2))
    else:
        form = QuadraticForm()

    data = {'a': a, 'b': b, 'c': c, 'txt': ', '.join(msg), 'disk': disk, 'form': form}

    return render(request, "quadratic/results.html", data)
