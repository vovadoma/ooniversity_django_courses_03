from django.shortcuts import render
from coaches.models import Coach

def detail(request, coach_id):
    coach = Coach.objects.get(id=coach_id)
    data = {'coach': coach}
    return render(request, 'coaches/detail.html', data)