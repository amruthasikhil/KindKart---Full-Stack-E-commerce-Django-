from django.urls import path
from Adminapp import views

urlpatterns=[
    path('homepage/',views.Adminhomepage,name="homepage"),
    path('viewcategories/',views.Viewcategories,name="viewcategories"),
    path('viewsubcategories/',views.Viewsubcategories,name="viewsubcategories"),
    path('viewproducts/',views.ViewProducts,name="viewproducts"),


    path('addcategories/',views.Addcategories,name="addcategories"),
     path('addcategoriespost/',views.Addcategoriespost,name="addcategoriespost"),
    path('deletecategory/<int:catid>',views.Deletecategories,name="deletecategory"),
    path('editcategory/<int:catid>',views.Editcategory,name="editcategory"),
    path('updatecategory/<int:catid>',views.Upadatecategorypost,name="updatecategory"),



    path('addsubcategories/',views.Addsubcategories,name="addsubcategories"),
     path('addsubcategoriespost/',views.Addsubcategoriespost,name="addsubcategoriespost"),
    path('deletesubcategory/<int:subid>',views.Deletesubcategories,name="deletesubcategory"),
     path('editsubcategory/<int:subid>',views.Editsubcategory,name="editsubcategory"),
    path('editsubcategorypost/<int:subid>',views.Upadatesubcategorypost,name="editsubcategorypost"),


    path('addroducts/',views.Addproducts,name="addproducts"),
    path('addroductspost/',views.Addproductspost,name="addroductspost"),
    path('deleteproduct/<int:pid>',views.Deleteproduct,name="deleteproduct"),
        path('editproduct/<int:pid>',views.Editproduct,name="editproduct"),
         path('editproductpost/<int:pid>',views.Editproductpost,name="editproductpost"),

  path('adminlogin/',views.Adminloginpage,name="adminlogin"),
  path('adminloginpost/',views.Adminloginpage_post,name="adminloginpost"),
 path('dashboard/',views.dashboard,name="dashboard"),

     path('addmember/',views.Addmember,name="addmember"),
      path('addmember_post/',views.Addmemberpost,name="addmember_post"),
 path('viewmember/',views.Viewmembers,name="viewmember"),
 path('userlogout/',views.Userlogout,name="userlogout"),

]