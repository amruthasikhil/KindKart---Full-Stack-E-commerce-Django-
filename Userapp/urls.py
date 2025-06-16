from django.urls import path
from Userapp import views

urlpatterns=[
    path('userhome/',views.Userhome,name="userhome"),
      path('userlogout/',views.Userslogout,name="userlogout"),

    path('userhome_productsearch/',views.Userhome_productsearch,name="userhome_productsearch"),

    path('',views.landingpage,name="landingpage"),

     path('landingpage_searchpost',views.landingpage_searchpost,name="landingpage_searchpost"),


    path('userregister/',views.Userregister,name="userregister"),
    path('userregisterpost/',views.Userregisterpost,name="userregisterpost"),
    path('usersign',views.Usersignin,name="usersign"),
    path('usersignpost/',views.Userloginpost,name="usersignpost"),



    path('mycart/',views.Userprofile,name="mycart"),
    path('Addtocart/',views.Addtocart,name="addtocart"),

     path('billingaddress/',views.billingaddress,name="billingaddress"),
     path('billingaddresspost/',views.billingaddresspost,name="billingaddresspost"),
     path('paymentnavigation/',views.Paymentnavigation,name="paymentnavigation"),


     path('adddonation/',views.Adddonation,name="adddonation"),
       path('adddonationpost/',views.Adddonationpost,name="adddonationpost"),


    path('editprofile/',views.Userprofileedit,name="editprofile"),
    path('editprofilepost/',views.Userprofileeditpost,name="editprofilepost"),


    path('productpageuser/',views.Productpageuser,name="productpageuser"),
     path('productpageuser_categorywise/<cname>',views.Productpageuser_categorywise,name="productpageuser_categorywise"),

     path('productpageuser_search/',views.Productpageuser_search,name="productpageuser_search"),
    path('singleproduct/<int:pid>',views.Singleproduct,name="singleproduct"),
   
    path('contactpage/',views.contactform,name="contactpage"),
    path('contactpagepost/',views.Contactpagepost,name="contactpagepost"),

    path('aboutpage/',views.aboutpage,name="aboutpage"),

]