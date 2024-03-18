from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader

from .models import Task,Profile
from .forms import CreateUserForm,LoginForm,CreateTaskForm,UpdateUserForm,UpdateProfileForm


from django.contrib.auth.models import auth,User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required

# Import Django messages (notifications)
from django.contrib import messages


def home(request):

    return render(request,'index.html')


   
# Create a Django admin user


def register(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():

            current_user =form.save(commit=False)

            form.save()

            profile = Profile.objects.create(user=current_user)

            messages.success(request,'User registration was sucessful!')

            return redirect('my-login')

    context = {'form':form}

    return render(request,'register.html',context=context)


# login a django user

def my_login(request):
    
    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')


            user =authenticate(request,username=username,password=password)

            if user is not None:

                auth.login(request, user)

                # return HttpResponse('You have logged in!')
                return redirect("dashboard")


    context ={'form' : form}

    return render(request,'my-login.html',context=context)


#  Dashboard page

@login_required(login_url='my-login')
def dashboard(request):

    profile_pic = Profile.objects.get(user=request.user)

    context ={'profile': profile_pic}

    return render(request,'profile/dashboard.html',context=context)


#  Profile management page

@login_required(login_url='my-login')
def profile_management(request):

    user_form =UpdateUserForm(instance=request.user)

    profile = Profile.objects.get(user=request.user)

    form_2 = UpdateProfileForm(instance=profile)

    if request.method == 'POST':

        user_form = UpdateUserForm(request.POST,instance=request.user)

        form_2 = UpdateProfileForm(request.POST, request.FILES,instance=profile)

        if user_form.is_valid():

            user_form.save()

            return redirect('dashboard')
        
        if form_2.is_valid():

            form_2.save()

            return redirect('dashboard')
        
    context = {'user_form': user_form, 'form_2': form_2}

    return render(request,'profile/profile-management.html',context=context)


#  Delete User account

@login_required(login_url='my-login')
def deleteAccount(request):

    if request.method == 'POST':

        deleteUser = User.objects.get(username=request.user)

        deleteUser.delete()

        return redirect('')
    
    return render(request,'profile/delete-account.html')
    


#  Create a task page

@login_required(login_url='my-login')
def createTask(request):
    
    form = CreateTaskForm()

    if request.method == 'POST':

        form = CreateTaskForm(request.POST)

        if form.is_valid():

            task = form.save(commit=False)

            task.user = request.user

            task.save()

            return redirect('view-tasks')
        
    context = {'form': form}

    return render(request,'profile/create-task.html',context=context)



#  View all tasks page

@login_required(login_url='my-login')
def viewTask(request):


    current_user = request.user.id

    task = Task.objects.all().filter(user=current_user)

    context = {'task':task}

    return render(request,'profile/view-tasks.html',context=context)



 #  Update tasks page

@login_required(login_url='my-login')
def updateTask(request,pk):

    task = Task.objects.get(id=pk)

    form = CreateTaskForm(instance=task)

    if request.method == 'POST':

        form = CreateTaskForm(request.POST, instance=task)

        if form.is_valid():

            form.save()

            return redirect('view-tasks')
        
    context = {'form':form}

    return render(request,'profile/update-task.html',context=context)


 #  Delete tasks page

@login_required(login_url='my-login')
def deleteTask(request,pk):

    task = Task.objects.get(id=pk)

    if request.method == 'POST':

        task.delete()

        return redirect('view-tasks')
    
    return render(request, 'profile/delete-task.html')




# logout a django user

def user_logout(request):

    auth.logout(request)

    return redirect ("")

