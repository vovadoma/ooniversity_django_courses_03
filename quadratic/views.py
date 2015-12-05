from django.shortcuts import render

from quadratic.forms import QuadraticForm


def quadratic_results(request):
    data = {}
    if request.GET:
        form = QuadraticForm(request.GET)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']

            ds = b ** 2 - 4 * a * c
            if ds > 0:
                x1 = float((-b + context['ds']**(1 / 2.0)) / (2 * a))
                x2 = float((-b - context['ds']**(1 / 2.0)) / (2 * a))
            elif ds == 0:
                x1 = x2 = float(-b / (2 * a))
            data = {'x1': x1, 'x2': x2, 'ds': ds}
    else:
        form = QuadraticForm()

    data['form'] = form
    return render(request, 'quadratic/results.html', data)
