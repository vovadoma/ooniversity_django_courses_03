from django.shortcuts import render

from quadratic.forms import QuadraticForm


def quadratic_results(request):
    data = {}
    if request.GET:

        form = QuadraticForm(request.GET)
        data['form'] = QuadraticForm(request.GET)
        if form.is_valid():

            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']

            data['ds'] = b ** 2 - 4 * a * c
            if data['ds'] > 0:
                data['x1'] = float(
                    (-b + data['ds']**(1 / 2.0)) / (2 * a))
                data['x2'] = float(
                    (-b - data['ds']**(1 / 2.0)) / (2 * a))
            elif int(data['ds']) == 0:
                data['x1'] = data[
                    'x2'] = float(-b / (2 * a))
    else:

        data['form'] = QuadraticForm()

    return render(request, 'quadratic/results.html', data)

