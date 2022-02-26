from django.shortcuts import render
from.models import student
# Create your views here.



def view(request):
    return render(request,'fruit.html')

def add(re):

    a = re.POST['n1']
    b = re.POST['n2']
    c = re.POST['n3']
    d  = re.POST['n4']
    e = re.FILES['n5']

    data = student(rollno=a, name=b, age=c, mark=d, image=e)
    data.save()
    return render(re, 'fruit.html')

def dis(re):


    data = student.objects.all()

    return render(re, 'fruit2.html', {'f': data})

def sea(re):
    return  render(re,'search.html')

def diss(re):
    l= re.POST['n6']

    data = student.objects.filter(rollno=l)


    return render(re,'searchd.html',{'f':data})

def update (re):
    l = re.POST['ro']
    m = re.POST['nam']
    i = re.POST['img']
    data = student.objects.filter(rollno=l)
    student.objects.filter(rollno=l).update(name=m,image=i)
    return render(re, 'UPDATE.html',{'f':data})
def delete (re):
    l = re.POST['ro']
    m = re.POST['nam']
    i = re.POST['img']
    data =student.objects.filter(rollno=l)

    data.delete()
    return render(re,'delete.html',{'f':data})