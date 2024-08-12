from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from . forms import Loginform,CreateUserForm,CreateRecordForm,UpdateRecordForm
from . models import Record
from django.contrib import messages
def home(request):
    return render(request,'webapp/index.html')




def login(request):
    form = Loginform()
    if request.method == "POST":
        form=Loginform(request,data = request.POST)
        if form.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password')
            user = authenticate(request, username=username ,password=password)
            # return redirect('')
            if user is not None:
                auth.login(request,user)
                return redirect('dashboard')
                
    context = {'login_form': form}
    return render(request,'webapp/my-login.html' ,context=context)

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'account created successfully ')
            return redirect('my-login')
            
    context = {'form': form}
    return render(request,'webapp/register.html' ,context=context)


def user_logout(request):
    auth.logout(request)
    messages.success(request,'Logout successfully ')
    
    return redirect('my-login')


@login_required(login_url='my-login')

def dashboard(request):
    my_record= Record.objects.all()
    context={'records':my_record}
    return render(request,'webapp/dashboard.html',context=context)



@login_required(login_url='my-login')

def create_record(request):
    form = CreateRecordForm()
    if request.method == "POST":
        form=CreateRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
        
    context={'create_form': form}
    return render(request,'webapp/create_record.html',context=context)
    
@login_required(login_url='my-login')
def update_record(request,pk):
    record =Record.objects.get(id=pk)
    form=UpdateRecordForm(instance=record)
    if request.method=='POST':
        form=UpdateRecordForm(request.POST,instance=record)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    context={'updateform':form}
    return render(request,'webapp/update-record.html',context=context)
    
@login_required(login_url='my-login')
def singular_record(request,pk):
    all_record=Record.objects.get(id=pk)
    context={'record':all_record}
    return render(request,'webapp/view-record.html',context=context)

@login_required(login_url='my-login')
def delete_record(request, pk):
    record = Record.objects.get(id=pk)
    record.delete()
    messages.success(request,'Record was deleted successfully ')
    
    return redirect ('dashboard')  # Redirect to a success page or a list view

# @login_required(login_url='my-login')
# def delete_modal_view(request, pk):
#     record = Record.objects.get( id=pk)
#     record.delete()
#     return render( request,' dashboard')