from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

from Adminapp.models import *
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage


#======================================================= categories
def Addcategories(request):
    obj=CategoriesDb.objects.all()

    return render(request,"addcategories.html",{"catobj":obj})

def Addcategoriespost(request):
    if request.method == "POST":
        category=request.POST.get("category")
        description=request.POST.get("description")
        print("-------------------------------------------------")
        obj=CategoriesDb(name=category,description=description)
        obj.save()
        return redirect(Addcategories)

def Viewcategories(request):
    obj=CategoriesDb.objects.all()
    return render(request,"viewcategories.html",{"data":obj,"catobj":obj})

def Deletecategories(request,catid):
    obj=CategoriesDb.objects.filter(id=catid)
    obj.delete()
    return redirect(Viewcategories)

def Editcategory(request,catid):
    obj=CategoriesDb.objects.get(id=catid)
    obj2=CategoriesDb.objects.all()
    return render(request,"edit_category.html",{"data":obj,"catobj":obj2})

def Upadatecategorypost(request,catid):
    if request.method == "POST":
        category=request.POST.get("category")
        description=request.POST.get("description")
        status=request.POST.get("status")
        obj=CategoriesDb.objects.filter(id=catid).update(name=category,description=description,availability=status)
        return redirect(Viewcategories)
    
#==========================================================================


def Addsubcategories(request):
    obj=CategoriesDb.objects.all()
    return render(request,"addsubcategories.html",{"data":obj,"catobj":obj})

def Addsubcategoriespost(request):
    if request.method == "POST":
        category=request.POST.get("category")
        subcategory=request.POST.get("subcategory")
        description=request.POST.get("description")
        print("-------------------------------------------------",category,subcategory,description)
        obj=SubcategoriesDb(name=subcategory,description=description,categories=category)
        obj.save()
        return redirect(Viewsubcategories)
    
def Deletesubcategories(request,subid):
    obj=SubcategoriesDb.objects.filter(id=subid)
    obj.delete()
    return redirect(Viewsubcategories)

def Editsubcategory(request,subid):
    obj=SubcategoriesDb.objects.get(id=subid)
    obj2=CategoriesDb.objects.all()
    return render(request,"edit_subcategory.html",{"data":obj,"catobj":obj2})


def Upadatesubcategorypost(request,subid):
    if request.method == "POST":
        category=request.POST.get("category")
        subcategory=request.POST.get("subcategory")
        description=request.POST.get("description")
        status=request.POST.get("status")
        obj=SubcategoriesDb.objects.filter(id=subid).update(name=subcategory,description=description,availability=status,categories=category)
        return redirect(Viewsubcategories)


def Addproducts(request):
    obj=SubcategoriesDb.objects.all()
    print(obj)
    catobj=CategoriesDb.objects.all()

    return render(request,"product.html",{"data":obj,"catobj":obj})

def Addproductspost(request):
    if request.method == "POST":
        name=request.POST.get("product")
        subcategories=request.POST.get("category")
        description=request.POST.get("description")
        condition=request.POST.get("level")
        image=request.FILES["imgg"]
        price=request.POST.get("price")
        obj=ProductDb(name=name,subcategories=subcategories,condition=condition,image=image,price=price,description=description)
        obj.save()
        print("okk")
        return redirect(Addproducts)

def Adminhomepage(request):
    obj=CategoriesDb.objects.all()
    
    return render(request,"index.html",{"catobj":obj})



def Editproduct(request,pid):
    obj=ProductDb.objects.get(id=pid)
    sub=SubcategoriesDb.objects.all()
    obj2=CategoriesDb.objects.all()
    return render(request,"editproduct.html",{"sub":sub,"data":obj,"catobj":obj2})

def Editproductpost(request,pid):
     if request.method == "POST":
        name = request.POST.get("product")
        subcategories = request.POST.get("category")
        description = request.POST.get("description")
        condition = request.POST.get("level")
        price = request.POST.get("price")

        try:
            imageb = request.FILES["imgg"]
            fs = FileSystemStorage()
            file = fs.save(imageb.name, imageb)  # Save new image
        except MultiValueDictKeyError:
            # If no new image is uploaded, use the existing image
            file = ProductDb.objects.get(id=pid).image

        # Update the product record in the database
        ProductDb.objects.filter(id=pid).update(
            name=name,
            description=description,
            image=file,  # Either new or existing image
            subcategories=subcategories,
            condition=condition,
            price=price
        )
        return redirect(ViewProducts)

def Deleteproduct(request,pid):
    obj=ProductDb.objects.filter(id=pid)
    obj.delete()
    return redirect(ViewProducts)

def Viewsubcategories(request):
    obj=SubcategoriesDb.objects.all()
    obj2=CategoriesDb.objects.all()
    return render(request,"viewsubcategories.html",{"data":obj,"catobj":obj2})

def ViewProducts(request):
    obj=ProductDb.objects.all()
    catobj=SubcategoriesDb.objects.all()
    obj2=CategoriesDb.objects.all()
    return render(request,"viewproducts.html",{"data":obj,"sub":catobj,"catobj":obj2})

def dashboard(request):
    catcount=CategoriesDb.objects.count()
    subcount=SubcategoriesDb.objects.count()
    prodcount=ProductDb.objects.count()
    return render(request,"dashboard.html",{"catcount":catcount,"subcount":subcount,"prodcount":prodcount})

def Adminloginpage(request):
    return render(request,"login.html")

def Adminloginpage_post(request):
     if request.method == "POST":
        un=request.POST.get('un')
        pswd=request.POST.get("pwd")
        if User.objects.filter(username__contains=un).exists():
            user=authenticate(username=un,password=pswd)
            if user is not None:
                request.session['username']=un
                request.session['password']=pswd
                login(request,user)
                return redirect(dashboard)
            else:
                return redirect(Adminloginpage)
        else:
            return redirect(Adminloginpage)
        

def Addmember(request):
    return render(request,"addmember.html")

def Addmemberpost(request):
    if request.method == "POST":
        name=request.POST.get("name")
        image=request.FILES["imgg"]
        designation=request.POST.get("duty")
        obj=MembersDb(name=name,pic=image,designation=designation)
        obj.save()
        print("okk")
        return redirect(Addmember)
    
def Viewmembers(request):
    obj=MembersDb.objects.all()
    return render(request,"viewmember.html",{"data":obj})

def Userlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(Adminloginpage)
# Create your views here.




