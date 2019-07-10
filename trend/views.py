from django.shortcuts import render,get_object_or_404
from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from django.shortcuts import render,redirect
from .models import Product,Profile,Comment
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from .forms import  UpdateProfileForm
def home(request):

    return render(request,'home.html')


@login_required(login_url='/accounts/login/')
def profile(request,id):
    current_user = request.user
    user = User.objects.get(id=id)
    products = Product.objects.filter(owner_id=id)
    if current_user.id == user.id:
        products = Product.objects.filter(owner_id=id)
        current_user = request.user
        user = User.objects.get(id=id)
        try:
            profile = Profile.objects.get(user_id=id)
        except ObjectDoesNotExist:
            return redirect(update_profile,current_user.id)
    else: 
        try:
            profile = Profile.objects.get(user_id=id)
        except ObjectDoesNotExist:
            
            return redirect(no_profile,id)      
            
    return render(request,'profile/profile.html',{'user':user,'profile':profile,'current_user':current_user,"products":products})

@login_required(login_url='/accounts/login/')
def update_profile(request,id):
    
    current_user = request.user
    user = User.objects.get(id=id)
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user_id=id
            profile.save()
            return redirect(home)
    else:
        form = UpdateProfileForm()
    return render(request,'profile/update_profile.html',{'user':user,'form':form})