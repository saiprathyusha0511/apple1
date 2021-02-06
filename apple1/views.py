from django.shortcuts import render
from django.http import HttpResponse
from apple1.forms import StudentForm
def demo(request):
	return HttpResponse('Iam from Apple1')



def reg(request):
	if request.method =='POST':
		form = StudentForm(request.POST)
		form.save()
		return HttpResponse('Data Inserted using Forms...')
	form = StudentForm()
	return render(request,'apple1/reg.html',{'form':form})
# Create your views here.
