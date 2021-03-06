from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from registration.models import Contingent,Data
from .models import Hall, Allotment
# Create your views here.

def index(request):
  return render(request, 'regdesk/login.html')
  
def contingent_id(request):
  
  context = {}
  
  if request.method == 'GET':
    con_id = request.GET.get("c_id")
    contingent_pk = Contingent.objects.get(captcha=con_id).pk
    students = Data.objects.filter(contingent=contingent_pk)
    
    checkedIn = []
    allotment_list = [obj.name for obj in Allotment.objects.all()]
    for student in students:
      if student.user in allotment_list:
        checkedIn.append(student)

    checkedIn_user = [obj.user for obj in checkedIn]

    students = students.exclude(user__in=checkedIn_user)
    students_male = students.filter(gender='M')
    male_num = students_male.count()
    male_halls = Hall.objects.filter(gender = 'M')
    
    students_female = students.filter(gender='F')
    female_num = students.filter(gender='F').count()
    female_halls = Hall.objects.filter(gender = 'F')

    

    context = {
      'students_male' : students_male,
      'students_female' : students_female,
      'male_num' : male_num,
      'female_num' : female_num,
      'captcha' : con_id,
      'female_halls' : female_halls,
      'male_halls' : male_halls,
      'checkedIn' : checkedIn,
    }
    
  return render(request, 'regdesk/details.html', context)


def hall_allotment(request):
  sum = 0
  if request.method == 'GET':
    con_id = request.GET.get("c_id")
    contingent_pk = Contingent.objects.get(captcha=con_id).pk
    students = Data.objects.filter(contingent=contingent_pk)
    
    for student in students:
      if (request.GET.get(str(student.pk))=='1'):
        sum += 1
        obj = Allotment()
        obj.name = student.user
        
        if (student.gender == "M"):
          hall = request.GET.get("m_hall")
          obj.hall = Hall.objects.get(name=hall)
        else:
          hall = request.GET.get("f_hall")
          obj.hall = Hall.objects.get(name=hall)
        
        obj.save()
        
    return HttpResponse(sum)
  
  else:
    return HttpResponse('Invalid Request')
        
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
    
    