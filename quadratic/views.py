# coding: utf-8
from django.shortcuts import render
import math

def quadratic_results(request):

    a = request.GET.get('a')
    b = request.GET.get('b')
    c = request.GET.get('c')

    msg = []
    dst = ''

    if a == '' or b == '' or c == '':
        msg.append(u'коэффициент не определен')

    if not (a.replace('-', '').isdigit() and b.replace('-', '').isdigit() and c.replace('-', '').isdigit()):
        msg.append(u'коэффициент не целое число')

    if a.replace('-', '').isdigit() and int(a) == 0:
        msg.append(u'коэффициент при первом слагаемом уравнения не может быть равным нулю')


    if not len(msg):
        a = int(a)
        b = int(b)
        c = int(c)

        ds = b * b - 4 * a * c
        dst = u'Дискриминант: %d' % ds

        if ds < 0:
            msg.append(u'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.')
        elif ds == 0:
            x1 = (-b + math.sqrt(ds)) / (2 * a)
            msg.append(u'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %s' % x1)
        else:
            x1 = (-b + math.sqrt(ds)) / (2 * a)
            x2 = (-b - math.sqrt(ds)) / (2 * a)
            msg.append(u'Квадратное уравнение имеет два действительных корня: x1 = %s, x2 = %s' % (x1, x2))

    data = {'a' : a, 'b' : b, 'c' : c, 'txt' : ', '.join(msg), 'dst' : dst}

    return render(request, "quadratic/results.html", data)
