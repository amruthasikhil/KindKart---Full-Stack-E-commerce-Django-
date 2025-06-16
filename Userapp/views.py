from django.shortcuts import render,redirect
from Adminapp.models import *
from Userapp.models import *
import razorpay
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage


def landingpage(request):
    obj=ProductDb.objects.all()[:6]
    catobj=CategoriesDb.objects.all()[:4]
    memeberobj=MembersDb.objects.all()
    return render(request,"landingpage.html",{"pdata":obj,"catobj":catobj,"member":memeberobj}) 


def landingpage_searchpost(request):
    if request.method == "POST":
        catobj=CategoriesDb.objects.all()[:4]
        memeberobj=MembersDb.objects.all()
        search=request.POST.get("search")
        obj=ProductDb.objects.filter(name__contains=search)[:6]
        return render(request,"landingpage.html",{"pdata":obj,"catobj":catobj,"member":memeberobj}) 


def Userhome(request):
    obj=ProductDb.objects.all()[:6]
    catobj=CategoriesDb.objects.all()[:4]
    memeberobj=MembersDb.objects.all()
    li=request.session['lid']
    cartcount=CartDb.objects.filter(userid=li)
    cartcount_no=cartcount.count()
    # x=request.session['lid']
    # userobj=UserDb.objects.get(id=x)
    catdata=[]
    for i in catobj:
        catgory=i.name
        pobj=SubcategoriesDb.objects.filter(categories=catgory)
        for i in pobj:

            catdata.append({
                "subcategory":i.name
            })
            print("============================",i.name)
    return render(request,"userindex.html",{"pdata":obj,"catobj":catobj,"member":memeberobj,"cartcount_no":cartcount_no})



def Userhome_productsearch(request):
    if request.method == "POST" :
        search=request.POST.get("search")
        obj=ProductDb.objects.filter(name__contains=search)[:6]
        catobj=CategoriesDb.objects.all()[:4]

        memeberobj=MembersDb.objects.all()
        # x=request.session['lid']
        # userobj=UserDb.objects.get(id=x)
        catdata=[]
        for i in catobj:
            catgory=i.name
            pobj=SubcategoriesDb.objects.filter(categories=catgory)
            for i in pobj:

                catdata.append({
                    "subcategory":i.name
                })
                print("============================",i.name)
        return render(request,"userindex.html",{"pdata":obj,"catobj":catobj,"member":memeberobj})


def contactform(request):
    obj=ProductDb.objects.all()[:3]
    catobj=CategoriesDb.objects.all()[:4]
    uid = request.session.get('lid')
    if uid:
            uid = request.session['lid']
            cartcount=CartDb.objects.filter(userid=uid)
            cartcount_no=cartcount.count()
            return render(request,"contact.html",{"pdata":obj,"catobj":catobj,"cartcount_no":cartcount_no})
    else:
        return render(request,"contact.html",{"pdata":obj,"catobj":catobj})
    
def Contactpagepost(request):
    if request.method == "POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        subject=request.POST.get("subject")
        phone=request.POST.get("phone")
        message=request.POST.get("message")
        print("**************************************************************")
        obj=ContactDb(name=name,email=email,subject=subject,message=message,phoneno=phone)
        obj.save()
    return redirect (contactform)





def aboutpage(request):
    obj=ProductDb.objects.all()[:3]
    catobj=CategoriesDb.objects.all()[:4]
    uid = request.session.get('lid')
    if uid:
            uid = request.session['lid']
            cartcount=CartDb.objects.filter(userid=uid)
            cartcount_no=cartcount.count()
            return render(request,"about.html",{"pdata":obj,"catobj":catobj,"cartcount_no":cartcount_no})
    else:
         return render(request,"about.html",{"pdata":obj,"catobj":catobj})


def Userprofile(request):
    x = request.session['lid']
    userobj = UserDb.objects.get(id=x)
    uid = request.session['lid']
    cartcount=CartDb.objects.filter(userid=uid)
    cartcount_no=cartcount.count()
    obj = CartDb.objects.filter(userid=uid)
    totamount=0
    print("------------------------------------------------", obj)
    
    newarr = []  
    
    for i in obj:
        pobj = ProductDb.objects.get(id=i.productid)
        totamount=totamount+i.totalprice
        newarr.append({
            "img": pobj.image,
            "totalprice": i.totalprice,
            "name": pobj.name,
             "subcategories": pobj.subcategories,
            "condition": pobj.condition
        })
    if totamount > 10:
        deliveryfees = 2
    else:
        deliveryfees = 5
    finalamount = totamount+deliveryfees
    request.session['subtotal']=totamount
    request.session['del_fees']=deliveryfees
    request.session['finalamount']=finalamount
    return render(request, "Mycart.html", {"userobj": userobj, "data": newarr,"cartcount_no":cartcount_no,"totamount":totamount,"deliveryfees":deliveryfees,"finalamount":finalamount})



def Productpageuser(request):
    obj=ProductDb.objects.all()
    catobj=CategoriesDb.objects.all()
    uid = request.session.get('lid')
    if uid:
        uid = request.session['lid']
        cartcount=CartDb.objects.filter(userid=uid)
        cartcount_no=cartcount.count()
        return render(request,"category.html",{"proobj":obj,"catobj":catobj,"cartcount_no":cartcount_no})
    else:
        return render(request,"category.html",{"proobj":obj,"catobj":catobj})
    

def Productpageuser_search(request):
    print("ok")
   
    if request.method == "POST":
        catobj=CategoriesDb.objects.all()
        search=request.POST.get("search")
        obj=ProductDb.objects.filter(name__contains=search)
        uid = request.session.get('lid')
        if uid:
            uid = request.session['lid']
            cartcount=CartDb.objects.filter(userid=uid)
            cartcount_no=cartcount.count()
            print("---------------------------------------------------------------------------------------------------------------------------")
            return render(request,"category.html",{"proobj":obj,"catobj":catobj,"cartcount_no":cartcount_no})
        else:
            return render(request,"category.html",{"proobj":obj,"catobj":catobj})


def billingaddresspost(request):
    if request.method == "POST":

        btn=request.POST.get("btn")
        if btn == "Save" :
            userid=request.session['lid']
            place=request.POST.get("place")
            pincode=request.POST.get("pincode")
            address=request.POST.get("address")
            obj=UserAddressDb(place=place,pincode=pincode,address=address,userid=userid)
            obj.save()
            return redirect(billingaddress)
        if btn == "Purchase":
            userid=request.session['lid']
            place=request.POST.get("place")
            address=request.POST.get("address")
            mobileno=request.POST.get("mobileno")
            pincode=request.POST.get("pincode")
            email=request.POST.get("email")
            subtotal=request.POST.get("subtotal")
            message=request.POST.get("message")
            obj=OrderDb(userid=userid,
                    email=email,
                    place=place,
                    address=address,
                    mobile=mobileno,
                    pin=pincode,
                    message=message,
                    totalPrice=subtotal
        )
        obj.save()
        return redirect(Paymentnavigation)

def billingaddress(request):
    uid = request.session['lid']
    cartcount=CartDb.objects.filter(userid=uid)
    cartcount_no=cartcount.count()
    subtotal=request.session['subtotal']
    user_details=UserDb.objects.get(id=uid)
    try:
        billaddress = UserAddressDb.objects.get(userid=uid)  
    except UserAddressDb.DoesNotExist:
        nodata = "no_data"  # Set this if no address is found
        billaddress = None  # Set to None if no address is found
    else:
        nodata = None  # Set `nodata` to None if address is found
    return render(request,"billing_address.html",{"subtotal":subtotal,"nodata":nodata,"cartcount_no":cartcount_no,"user_details":user_details,"billaddress":billaddress})
# def Deletefromcart




def Paymentnavigation(request):
    uid=request.session['lid']
    obj=OrderDb.objects.get(userid=uid)
    customername_ob=UserDb.objects.get(id=uid)
    customer=customername_ob.name
    totalamount=obj.totalPrice

    cartcount=CartDb.objects.filter(userid=uid)
    cartcount_no=cartcount.count()
    #convert amount into paisa
    amoount=int(totalamount*100)

    amount_str=str(amoount)

    if request.method == "POST":
        order_currency = 'INR'
        client =razorpay.Client(auth=('rzp_test_MMwua6oGM7f6Bi','FYZEoZkAuia58N8GlRTUGAkE'))
        payment=client.order.create({'amount':amoount,'currency': order_currency})
    return render(request,"paymentnavigation.html",{'amount_str':amount_str,"customer":customer,"cartcount_no":cartcount_no,})

def Productpageuser_categorywise(request,cname):
    category_choosen = cname
    
    subcateg = SubcategoriesDb.objects.filter(categories=category_choosen)
    subcategory_names = subcateg.values_list('name', flat=True)  # Get list of subcategory names

    obj = ProductDb.objects.filter(subcategories__in=subcategory_names)  # Filter by subcategory names
    print("Filtered Products:")
    for product in obj:
        print(f"ID: {product.id}, Name: {product.name}, Price: {product.price}, Subcategory: {product.subcategories}")

    # [("Living Room Furniture",), ("Bedroom Furniture",)]
    # ["Living Room Furniture", "Bedroom Furniture"]    

    catobj=CategoriesDb.objects.all()[:4]
    return render(request,"categorywiseproduct.html",{"proobj":obj,"catobj":catobj})


def Addtocart(request):
    if request.method == "POST":
        productid=request.POST.get("productid")
        productprice=request.POST.get("productprice")
        productimg=request.POST.get("productimg")
        userid=request.session['lid']
        obj=CartDb(userid=userid,productid=productid,totalprice=productprice,pimg=productimg)
        obj.save()
        return redirect(Userhome)
    
# def Viewcart(request):
#     uid=request.session['lid']
#     obj=CartDb.objects.filter(userid=uid)
#     newarr=[]
#     for i in obj:
#         pobj=ProductDb.objects.get(id=i.productid)

#         newarr=[{
#             "img":obj.pimg,
#             "totalprice":obj.totalprice,
#             "name":i.name
#         }]

#     return render 

def Singleproduct(request,pid):
    obj=ProductDb.objects.get(id=pid)
    return render(request,"singleproduct.html",{"pobj":obj})

def Userregister(request):
    return render(request,"userregister.html")

def Userregisterpost(request):
    print("================")
    if request.method == "POST":
        print("==yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy==============")
        name=request.POST.get("name")
        phone=request.POST.get("mob")
        email=request.POST.get("email")
        image=request.FILES["imgg"]
        password=request.POST.get("pwd")
        obj=UserDb(name=name,mob=phone,email=email,pic=image,password=password)
        obj.save()
        return redirect(Userregister)
    else:
        return render(request,"userregister.html")

def Usersignin(request):
    return render(request,"usersignin.html")



def Userloginpost(request):
    if request.method == "POST":
        uname = request.POST.get("email")
        pwd = request.POST.get("password")
        
        x = UserDb.objects.filter(email=uname, password=pwd)
        
        if x.exists():
            user = x.first()  
            request.session['lid'] = user.id  
            print(user.id,"***************************************************************")
            return redirect(Userhome) 
        else:
            return redirect(Usersignin) 
    else:
        return redirect(Usersignin)
    
def Userprofileedit(request):
    x=request.session['lid']
    userobj=UserDb.objects.get(id=x)
    uid = request.session['lid']
    cartcount=CartDb.objects.filter(userid=uid)
    cartcount_no=cartcount.count()
    return render(request,"edit_profile.html",{"userobj":userobj,"cartcount_no":cartcount_no})

def Userprofileeditpost(request):
        x=request.session['lid']
        if request.method == "POST":
            name=request.POST.get("name")
            phone=request.POST.get("phone")
            email=request.POST.get("email")
            try:
                print("=====")
                image=request.FILES["imgg"]
                print("yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy")
                fs=FileSystemStorage()
                file=fs.save(image.name,image)
                print("---------////////////////////////////////////////////////////-------------------------")
            except MultiValueDictKeyError:
                file=UserDb.objects.get(id=x).pic
                print(file)
            UserDb.objects.filter(id=x).update(name=name,email=email,mob=phone,pic=file)
            return redirect(Userprofileedit)
        else:
            return redirect(Userprofileedit)

def Categorywiseproduct(request,catname):
    obj=ProductDb.objects.all()
    return render(request,"category.html",{"proobj":obj})

def Adddonation(request):
    obj=SubcategoriesDb.objects.all()
    print(obj)
    catobj=CategoriesDb.objects.all()
    return render(request,"givedonations.html",{"data":obj})

def Adddonationpost(request):
    if request.method == "POST":
        name=request.POST.get("product")
        subcategories=request.POST.get("category")
        description=request.POST.get("description")
        condition=request.POST.get("level")
        image=request.FILES["imgg"]
        price=request.POST.get("price")
        obj=ProductDb(name=name,subcategories=subcategories,condition=condition,image=image,price=price,description=description,availability="not_availability")
        obj.save()
        print("okk")
        return redirect(Adddonation)
    
def Userslogout(request):
    del request.session['lid']
    return redirect(landingpage)