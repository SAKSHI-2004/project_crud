from django.shortcuts import render,redirect
from .models import student
from django.contrib import messages


def index(request):
    data=student.objects.all()
    print(data)
    context={"data":data}
    return render(request,"index.html",context)


def about(request):
    return render(request,"about.html")





def insert(request):
   
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        print(name, email , age , gender)
        query=student(name =name , email = email, age = age ,  gender = gender)
        query.save()

    return render(request,"index.html" )

def update(request,id):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        age=request.POST['age']
        gender=request.POST['gender']

        edit=student.objects.get(id=id)
        edit.name=name
        edit.email=email
        edit.gender=gender
        edit.age=age
        edit.save()
        messages.warning(request,"Data Updated Successfully")
        return redirect("/")

    d=student.objects.get(id=id) 
    context={"d":d}
    return render(request,"edit.html",context)

def delete(request,id):
    d=student.objects.get(id=id) 
    d.delete()
    messages.error(request,"Data deleted Successfully")
    return redirect("/")
    

