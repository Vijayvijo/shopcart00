<<<<<<< HEAD
from django.shortcuts import render,redirect
from .models import *
from shop.form import CustomUserForm
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate,login,logout
import json
from django.db import IntegrityError



# Create your views here.

def Home(request):
    products = Product.objects.filter(trending=1)
    return render(request,"shop/index.html",{"products": products})

def cart_page(request):
    if request.user.is_authenticated:
        cart=Cart.objects.filter(user=request.user)
        return render(request,"shop/cart.html",{"cart": cart})

    else:
        return redirect("/")
    
def remove_fav(request,fid):
    cart_item = Favourite.objects.get(id=fid)
    cart_item.delete()
    return redirect("/favviewpage/")
    
def remove_cart(request,cid):
    cart_item = Cart.objects.get(id=cid)
    cart_item.delete()
    return redirect("/cart/")

def favviewpage(request):
    if request.user.is_authenticated:
        fav=Favourite.objects.filter(user=request.user)
        return render(request,"shop/fav.html",{"fav":fav})
    else:
        return redirect("/")


def fav_page(request):
        if request.method == "POST":
            product_qty = request.POST.get('product_qty')

        # Debugging: Check if product_qty is received
        print("Received product_qty:", product_qty)

        if not product_qty:  # If product_qty is missing or empty
            return JsonResponse({"error": "Product quantity is required"}, status=400)

        try:
            # Save the data to the database
            favorite = Favorite.objects.create(product_qty=product_qty)
            return JsonResponse({"message": "Product added to favorites"}, status=200)
        
        except IntegrityError as e:
            return JsonResponse({"error": "Database Integrity Error", "details": str(e)}, status=400)
    
        #  return JsonResponse({"error": "Invalid request method"}, status=405)

def add_to_cart(request):
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":  
        if request.user.is_authenticated:
            try:
                data = json.loads(request.body)  
                product_qty = int(data.get("product_qty", 1))
                product_id = data.get("pid")

                product = Product.objects.filter(id=product_id).first()  
                if not product:
                    return JsonResponse({"status": "Product Not Found"}, status=404)

                # Check if the product is already in the cart
                existing_cart_item = Cart.objects.filter(user=request.user, product_id=product_id).first()
                if existing_cart_item:
                    return JsonResponse({"status": "Product Already in Cart"}, status=200)

                # Check stock availability
                if product.quantity >= product_qty:
                    Cart.objects.create(user=request.user, product_id=product_id, product_qty=product_qty)
                    return JsonResponse({"status": "Product Added to Cart"}, status=200)
                else:
                    return JsonResponse({"status": "Product Stock Not Available"}, status=400)
            except json.JSONDecodeError:
                return JsonResponse({"status": "Invalid JSON Data"}, status=400)
        else:
            return JsonResponse({"status": "Login to Add Cart"}, status=401)
    else:
        return JsonResponse({"status": "Invalid Access"}, status=403)




def logout_page(request):
        if request.user.is_authenticated:
            logout(request)
        messages.success(request,"Logged out Successfully")
        return redirect("/")

def login_page(request):
    if request.user.is_authenticated:
     return redirect("/")   
    else:
        if request.method == 'POST':
            name=request. POST.get('username')
            pwd=request.POST.get('password')
            user=authenticate (request, username=name, password=pwd)
            if user is not None:
                login (request, user)
                messages.success (request, "Logged in Successfully")
                return redirect("/")
            else:
                messages.error(request, "Invalid User Name or Password")
                return redirect("/login")
        return render(request, "shop/login.html")
    
def register(request):
    form = CustomUserForm()
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration Success you can Login now")
            return redirect('/login')
    return render(request,"shop/register.html",{'form':form})

def collections(request):
    category = Category.objects.filter(status=0)
    return render(request,"shop/collections.html",{"category":category})
    

def collectionsview(request, name):
    if Category.objects.filter(name=name, status=0).exists():
        products = Product.objects.filter(category__name=name)
        
        # Check if any product has missing images and provide a default
        for product in products:
            if not product.product_image:  # If no image is assigned
                product.product_image = "img2.jpg"  # Change to your default image

        return render(request, "shop/products/index.html", {"products": products,"category_name":name})
    
    else:
        messages.warning(request, "No Such Category Found")
        return redirect('collections')

def product_details(request,cname,pname):
    if(Category.objects.filter(name=cname,status=0)):
        if(Product.objects.filter(name=pname,status=0)):
         products=Product.objects.filter(name=pname,status=0).first()
         return render(request,"shop/products/product_details.html",{"products":products})
     
        else:
            messages.error(request,"No such product Found")
            return redirect('collections')
    else:
     messages.error(request,"No such Category Found")
    return redirect('collections')


=======
from django.shortcuts import render,redirect
from .models import *
from shop.form import CustomUserForm
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate,login,logout
import json
from django.db import IntegrityError



# Create your views here.

def Home(request):
    products = Product.objects.filter(trending=1)
    return render(request,"shop/index.html",{"products": products})

def cart_page(request):
    if request.user.is_authenticated:
        cart=Cart.objects.filter(user=request.user)
        return render(request,"shop/cart.html",{"cart": cart})

    else:
        return redirect("/")
    
def remove_fav(request,fid):
    cart_item = Favourite.objects.get(id=fid)
    cart_item.delete()
    return redirect("/favviewpage/")
    
def remove_cart(request,cid):
    cart_item = Cart.objects.get(id=cid)
    cart_item.delete()
    return redirect("/cart/")

def favviewpage(request):
    if request.user.is_authenticated:
        fav=Favourite.objects.filter(user=request.user)
        return render(request,"shop/fav.html",{"fav":fav})
    else:
        return redirect("/")


def fav_page(request):
        if request.method == "POST":
            product_qty = request.POST.get('product_qty')

        # Debugging: Check if product_qty is received
        print("Received product_qty:", product_qty)

        if not product_qty:  # If product_qty is missing or empty
            return JsonResponse({"error": "Product quantity is required"}, status=400)

        try:
            # Save the data to the database
            favorite = Favorite.objects.create(product_qty=product_qty)
            return JsonResponse({"message": "Product added to favorites"}, status=200)
        
        except IntegrityError as e:
            return JsonResponse({"error": "Database Integrity Error", "details": str(e)}, status=400)
    
        #  return JsonResponse({"error": "Invalid request method"}, status=405)

def add_to_cart(request):
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":  
        if request.user.is_authenticated:
            try:
                data = json.loads(request.body)  
                product_qty = int(data.get("product_qty", 1))
                product_id = data.get("pid")

                product = Product.objects.filter(id=product_id).first()  
                if not product:
                    return JsonResponse({"status": "Product Not Found"}, status=404)

                # Check if the product is already in the cart
                existing_cart_item = Cart.objects.filter(user=request.user, product_id=product_id).first()
                if existing_cart_item:
                    return JsonResponse({"status": "Product Already in Cart"}, status=200)

                # Check stock availability
                if product.quantity >= product_qty:
                    Cart.objects.create(user=request.user, product_id=product_id, product_qty=product_qty)
                    return JsonResponse({"status": "Product Added to Cart"}, status=200)
                else:
                    return JsonResponse({"status": "Product Stock Not Available"}, status=400)
            except json.JSONDecodeError:
                return JsonResponse({"status": "Invalid JSON Data"}, status=400)
        else:
            return JsonResponse({"status": "Login to Add Cart"}, status=401)
    else:
        return JsonResponse({"status": "Invalid Access"}, status=403)




def logout_page(request):
        if request.user.is_authenticated:
            logout(request)
        messages.success(request,"Logged out Successfully")
        return redirect("/")

def login_page(request):
    if request.user.is_authenticated:
     return redirect("/")   
    else:
        if request.method == 'POST':
            name=request. POST.get('username')
            pwd=request.POST.get('password')
            user=authenticate (request, username=name, password=pwd)
            if user is not None:
                login (request, user)
                messages.success (request, "Logged in Successfully")
                return redirect("/")
            else:
                messages.error(request, "Invalid User Name or Password")
                return redirect("/login")
        return render(request, "shop/login.html")
    
def register(request):
    form = CustomUserForm()
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration Success you can Login now")
            return redirect('/login')
    return render(request,"shop/register.html",{'form':form})

def collections(request):
    category = Category.objects.filter(status=0)
    return render(request,"shop/collections.html",{"category":category})
    

def collectionsview(request, name):
    if Category.objects.filter(name=name, status=0).exists():
        products = Product.objects.filter(category__name=name)
        
        # Check if any product has missing images and provide a default
        for product in products:
            if not product.product_image:  # If no image is assigned
                product.product_image = "img2.jpg"  # Change to your default image

        return render(request, "shop/products/index.html", {"products": products,"category_name":name})
    
    else:
        messages.warning(request, "No Such Category Found")
        return redirect('collections')

def product_details(request,cname,pname):
    if(Category.objects.filter(name=cname,status=0)):
        if(Product.objects.filter(name=pname,status=0)):
         products=Product.objects.filter(name=pname,status=0).first()
         return render(request,"shop/products/product_details.html",{"products":products})
     
        else:
            messages.error(request,"No such product Found")
            return redirect('collections')
    else:
     messages.error(request,"No such Category Found")
    return redirect('collections')


>>>>>>> e7df23b (second commit)
