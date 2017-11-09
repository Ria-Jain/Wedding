from django.shortcuts import render, redirect
from .models import Wishe
# Create your views here.
def index(request):
	context={}
	if request.method=='POST':
		author=request.POST['author']
		message=request.POST['message']
		wish = Wishe.objects.create(
						author=author,
						text=message,
					)
		wish.save()
		return redirect('/')
	else:
		wishes=Wishe.objects.order_by('-created_date')
		print(wishes)
		context['wishes']=wishes
		return render(request,'index.html', context)