from django.shortcuts import render
from coaches.models import Coach

def detail(request, coach_id):
    coach = Coach.objects.get(id=coach_id)
    data = {'coach': coach}
    print coach.coach_courses.all()
    return render(request, 'coaches/detail.html', data)