from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.decorators import login_required



def registerPage(request):

	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

			

			messages.success(request, 'Account was created for ' + username)

			return redirect('login')
		

	context = {'form':form}
	return render(request, 'capp/register.html', context)


def loginPage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'capp/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

def home(request):

    categories= category.objects.all()
    context={'user' : request.user,'categories':categories}

    return render(request,'capp/dashboard.html',context)

def product1(request,pk):
    cate = category.objects.get(id=pk)
    products= product.objects.filter(categories=cate)
    context={'products':products,'cate':cate}
    return render(request,'capp/menu.html',context)
a=" " 


def addtocart(request,itemid):
    user = request.user
    quentity = request.POST['quantity']
    products = product.objects.get(id = itemid)
    carts=cart.objects.all()
    b=carts.count()
    if float(quentity) < 1.0:
        messages.add_message(request,messages.INFO,'Minimum quantity should be 1')
        return redirect('home')
    else:
        products.quantity = quentity
        
    products.amount=float(quentity)*products.price
    
    products.save()
    #m=products.restaurants.resname
    
    
    
    cart(user = user,product = products).save()
        #a=cart1.product.categories.resname
       

    

    

    
   
    return redirect(request.META['HTTP_REFERER'])
c=0.0





def cartview(request):
    global c
    cartitems = cart.objects.filter(user=request.user)
    c=0.0
    for i in cartitems:
        
        c += i.product.amount 

    
    return render(request,"capp/cart.html",{'cartitems' : cartitems,'c':c})



def deletefromcart(request,cartid):
    global c
    cart.objects.get(id = cartid).delete()
    return redirect(request.META['HTTP_REFERER'])



def placeorder(request):
    global c
    products = [" x ".join([z.product.dname,str(z.product.quantity)]) for z in cart.objects.filter(user = request.user)]
    for i in cart.objects.filter(user=request.user):
        name=i.product.categories
    c=0.0
    for i in cart.objects.filter(user=request.user):
        
        c += i.product.amount     

    order(user = request.user,items= "\n".join(products),categories=name,total=c).save()

    messages.add_message(request,messages.INFO,'Your order is succesfully placed')
    for i in cart.objects.filter(user = request.user):
        i.delete()
    c=0.0
    return redirect('home')



def ordersview(request):
    orders = []
    for i in order.objects.filter(user = request.user):
        orders.append(i)
    context = {'orders' : orders}
    return render(request,"capp/orders.html",context)


def searchview(request):
    search = request.POST['search']
    #items = [item for item in menu.objects.all() if item.dname.find(search)!=-1]
    categories = [res for res in category.objects.all() if res.resname.find(search)!=-1]
    
    context = {'categories':categories}
    return render(request,"capp/dashboard.html",context)


    




	