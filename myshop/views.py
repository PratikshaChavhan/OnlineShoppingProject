from django.shortcuts import render,redirect,HttpResponse
from.forms import UserForm,UserUpdationForm
from django.contrib.auth import authenticate,login,logout
from .models import MyImage,Category,Product,User,Cart,Order,FeedBack


# Create your views here.

CategoryList=Category.objects.all()
ProductList=Product.objects.all()

def home(request):
    UserName=request.session.get('UserName')
    d={'cl':CategoryList, 'pl':ProductList,'uname':UserName}
    return render(request,"home.html",d)

def addUser(request):
    if request.method=='POST':
        
        u=UserForm(request.POST)
        u.save()
        return redirect("/")
    else:    
        
        u=UserForm
        d={ 'cl':CategoryList ,'form':u}   
        return render(request,"myform.html",d)


def Mylogin(request):       
    d={ 'cl':CategoryList}   
    if request.method=='POST':
        uname=request.POST.get('uname')
        passw=request.POST.get('passw')
        usr=authenticate(request,username=uname,password=passw)
        if usr is not None:
            request.session['UserName']=uname
            UserName=request.session.get('UserName')
            login(request,usr)
            return redirect("/")
        else:
            return HttpResponse("<h2>Invalid UserName and password</h2>")    
    else:
        return render(request,"login.html")  


def editUser(request):
    UserName=request.session.get('UserName')
    usr=User.objects.get(username=UserName)
    if request.method=='POST':
        u=UserUpdationForm(request.POST,instance=usr)
        u.save()
        return redirect("/")
    else:    
        u=UserUpdationForm(instance=usr)#use userform edit all profile with passward
        d={'cl':CategoryList,'form':u}
        return render(request,'editprofile.html',d)


def logOut(request):
    logout(request)
    return redirect("/")     

def getbyCategory(request):
    cid=request.GET.get("cid")
    pl=Product.objects.filter( Category_id=cid)
    d={ 'cl':CategoryList , 'pl':pl}
    return render(request,'home.html',d)

def searchPage(request):
    d={ 'cl':CategoryList , 'pl':ProductList}
    return render(request,'searchPage.html',d)           

def search(request):
    sp=request.POST.get('sp')
    pl=Product.objects.filter(Pname__icontains=sp)
    d={ 'cl':CategoryList , 'pl':pl}
    return render(request,'searchPage.html',d)  

def AddCart(request):
    id=request.GET.get('id')
    prd=Product.objects.get(id=id)
    UserName=request.session.get('UserName')
    usr=User.objects.get(username=UserName)
    cart=Cart()
    cart.Product=prd
    cart.User=usr
    cart.save()
    return redirect("/")         
    
def cartList(request):
    UserName=request.session.get('UserName')
    usr=User.objects.get(username=UserName)
    if request.method=="POST":
        ord=Order()
        ord.User=usr
        totalBill=request.POST.get("totalBill")
        ord.totalBill=totalBill
        ord.save()
        print("-----------------",totalBill)
        crlist=Cart.objects.filter(User_id=usr.id)        
        for cr in crlist:
            cr.delete()

        return redirect("ordered.html")
    else:
        crlist=Cart.objects.filter(User_id=usr.id)
        totalBill=0
        for b in crlist:
            totalBill=totalBill+b.Product.Price

        d={'cl':CategoryList,'crlist':crlist,'totalBill':totalBill}
        return render(request,'CartList.html',d)

def ordered(request):
    UserName=request.session.get('UserName')    
    usr=User.objects.get(username=UserName)
    crlist=Cart.objects.filter(User_id=usr.id)
    
    ordlist=Order.objects.all()
    d={ 'cl':CategoryList , 'ordlist':ordlist }
    return render(request,'ordered.html',d)  
    

def productlist(request):
    prdlist=Product.objects.all()
    #pl=Product.objects.filter(Pname__icontains=sp)
    d={ 'cl':CategoryList , 'prdlist':prdlist}
    return render(request,'productlist.html',d)  


from .forms import MyImageForm
def checkimage(request):
    if request.method=='POST':
        f=MyImageForm(request.POST,request.FILES)
        f.save()
        f=MyImageForm
        img=MyImage.objects.all()
        d={'img':img,'form':f}
        return render(request,'checkimage.html',d)    
    else:
        f=MyImageForm
        img=MyImage.objects.all()
        d={'img':img,'form':f}
        return render(request,'checkimage.html',d)    

