from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages

# Create your views here.
flag = False

def Login(request):
    if request.method =="POST":
        data = request.POST
        login_email = data.get('email')
        password = data.get('password')
      
        signup_data = Signup_Db.objects.all()
        for x in signup_data:
            if x.email == login_email and x.password == password:
                request.session['email'] = login_email
                global flag
                flag = True
                request.session['flag'] = True
                return redirect('http://127.0.0.1:8000/admin-panel/')
     
        
        messages.error(request, 'Email OR Password is Incorrect !')
        return redirect("http://127.0.0.1:8000/login/")
        
    context = {"flag":flag}         
    return render(request, "login.html", context)


def Signup(request):
    if request.method =="POST":
        data = request.POST
        full_Name = data.get('full_name')
        email = data.get('email')
        password = data.get('password')
        confirm = data.get('confirm')
        if password == confirm:
            signup_data = Signup_Db.objects.all()
            for x in signup_data:
                if x.email == email:
                    messages.info(request, 'Email is Already Registered !')
                    return redirect("http://127.0.0.1:8000/sign-up/")
            Signup_Db.objects.create(name=full_Name,email=email,password=password)
            request.session['email'] = email
            global flag
            flag = True
            return redirect("http://127.0.0.1:8000/admin-panel/")
        else:
            
            messages.error(request, 'Confirmation Password not Match !')
    context = {"flag":flag}    
    return render(request, "signup.html", context)


def Admin_Panel(request):
    
    login_or_signup_email = request.session['email']
    admin_panel_auth = flag
    if request.method == "POST":
        data = request.POST
        recipe_Name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_Image = request.FILES.get('recipe_image')
        print(recipe_Name, recipe_description, recipe_Image)
        Admin_Panel_Db.objects.create(login_or_signup_email=login_or_signup_email, recipe_name=recipe_Name, recipe_dscription=recipe_description, recipe_image=recipe_Image)
    all_Data = Admin_Panel_Db.objects.filter(login_or_signup_email=login_or_signup_email)
    
    context = {"all_Data":all_Data, "admin_panel_auth":admin_panel_auth, "flag":flag}

    return render(request, "admin-panel.html", context)
   

def Delete(request, id):
    queryset = Admin_Panel_Db.objects.get(id = id)
    queryset.delete()
    return redirect('http://127.0.0.1:8000/admin-panel/')


def Edit_Recipe(request, id):
    queryset = Admin_Panel_Db.objects.get(id=id)
    print(id)
    if request.method == "POST":
        data = request.POST

        recipe_Name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_Image = request.FILES.get('recipe_image')

        queryset.recipe_name = recipe_Name
        queryset.recipe_dscription = recipe_description
        if recipe_Image:
            queryset.recipe_image = recipe_Image

        queryset.save()
        return redirect('http://127.0.0.1:8000/admin-panel/')

    
    context = {"queryset":queryset, "flag":flag} 
    return render(request, "edit_recipe.html", context)




def Home(request):
    global flag
    all_data = Admin_Panel_Db.objects.all().order_by('-id')
    context = {"flag":flag, "all_data":all_data}
    return render(request, "home.html", context)
    
def ReadMore(request, id):
    specific_data = Admin_Panel_Db.objects.get(id=id)
    context = {"specific_data":specific_data}
    return render(request, "readmore.html", context)
    
def Logout_Function(request):
    global flag
    flag = False
    context= {"flag":flag}
    return redirect('http://127.0.0.1:8000/', context)

