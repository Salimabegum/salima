from django.shortcuts import render,redirect,HttpResponse
from .models import Product_field,user_field, buyed
# Create your views here.

def product_field(request):
	if request.method=="POST":
		name = request.POST['name']
		description = request.POST['description']
		cost = request.POST['cost']
		no_of_product = request.POST['no_of_product']
		Product_field.objects.create(name=name,description=description,cost=cost,no_of_product=no_of_product)
		return redirect('homepage')
	return render(request,'Product_field.html')

def homepage(request):
	data = Product_field.objects.all()
	return render(request,'homepage.html',{'details':data})	

def dest(request,id):
	data = Product_field.objects.get(id=id)
	data.delete()
	return redirect('homepage')	

def homepage1(request,id):
	product = Product_field.objects.get(id = id)
	if request.method=="POST":
		email = request.POST['email']
		data = user_field.objects.get(email=email)
		if data.Account_blnc>product.cost:
			data.Account_blnc = data.Account_blnc-product.cost
			data.save()
			buyed.objects.create(product=product, user=data)
			return render(request,'single.html',{'details':data})
		else:
			return HttpResponse('You do not have sufficient Money!')	
		# return redirect('homepage2')
	return render(request,'homepage1.html',{'details':product})



def User_field(request):
	if request.method=="POST":
		Username = request.POST['Username']
		email = request.POST['email']
		mobile = request.POST['mobile']
		Account_blnc = request.POST['Account_blnc']
		user_field.objects.create(Username=Username,email=email,mobile=mobile,Account_blnc=Account_blnc)
		return redirect('homepage2')
	return render(request,'User_field.html')

def single(request,id):
	data = user_field.objects.get(id=id)
	return render(request,'single.html',{'details':data})

def homepage2(request):
	data1 = user_field.objects.all()
	return render(request,'homepage2.html',{'details':data1})		


def destroy(request,id):
	data=user_field.objects.get(id=id)
	data.delete()
	return redirect('homepage2')


def buy_user(request,id):
	user = user_field.objects.get(id=id)
	return render(request,'homepage1.html', {"details": user})

def homepage3(request,id):
	data = user_field.objects.get(id=id)
	if Account_blnc>0:
			Account_blnc = Account_blnc-cost
			return HttpResponse("Account_blnc is"+Account_blnc)
	else:
		return HttpResponse("Your Account_blnc is not sufficient")
	return render(request,'homepage3.html',{'details':data})

