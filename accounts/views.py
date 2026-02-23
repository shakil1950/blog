import uuid
from django.contrib.auth.views import PasswordResetView
from django.utils.text import slugify
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect,JsonResponse
from django.contrib import messages
from .forms import RegistrationForm,UserEditForm,ProfileEditForm,ChangePaswordForm
from django.contrib import auth
from django.contrib.auth.hashers import check_password
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile
from blogs.models import Blog
from dashboard.forms import PostForm
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_str
from django.contrib.sites.shortcuts import get_current_site


def registration(request):

    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form_save=form.save(commit=False)
            form_save.is_active=False
            form_save.save()
            form=RegistrationForm()
            token=default_token_generator.make_token(form_save)
            uid=urlsafe_base64_encode(force_bytes(form_save.pk))
            domain=get_current_site(request).domain
            
            link=f"http://{domain}/accounts/activate/{uid}/{token}/"
            send_mail(
                        'Account Activation',
                        f'হ্যালো {form_save.username}, আপনার আইডি এক্টিভ করতে এই লিঙ্কে ক্লিক করুন:{link} ',
                        'shakilahmed.pbl@gmail.com',
                        [form_save.email],
                    )
            messages.success(request,'Please check your email to activate your account')
            return redirect('home')
        else:
            print(form.errors)
    else:
        form=RegistrationForm()
    context={
        'form':form
    }
    return render(request,'authentication/registration.html',context)

def activate_user(request,uid64,token):
    try:
        uid=force_str(urlsafe_base64_decode(uid64))
        user=User.objects.get(id=uid)
    except(TypeError,ValueError,OverflowError,User.DoesNotExist):
        user=None
    if user is not None and default_token_generator.check_token(user,token):

        user.is_active=True
        user.save()
        messages.success(request,'Account activated')
        return redirect('login')


def login(request):

    if request.method=='POST':
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=auth.authenticate(username=username,password=password)
            if  user is not None:
                auth.login(request,user)
                if 'next' in request.POST and request.POST.get('next'):
                    return redirect(request.POST.get('next'))
                return redirect('profile')
            else:
                return redirect('login')
    form=AuthenticationForm()
    context={
        'form':form
    }
    return render(request,'authentication/login.html',context)

@login_required
def logout(request):
    auth.logout(request)
    return redirect('login')


@login_required
def profile(request):
    # info=Profile.objects.get(user=request.user)
    prof=Profile.objects.get(user=request.user)
    userform = UserEditForm(instance=request.user)
    profileForm = ProfileEditForm(instance=prof)
    context={
        'userform':userform,
        'profileForm':profileForm
    }

    return render(request,'authentication/profile.html',context)

@login_required
def profile_wise_post(request):
    try:
        
        posts=Blog.objects.filter(author=request.user)
        number_of_post=posts.count()
        latest=posts.latest('created_at').created_at
        draft=Blog.objects.filter(status='Draft',author=request.user).count()
        published_post=number_of_post-draft
        form=PostForm()
        if request.method=='POST':
            form=PostForm(request.POST,request.FILES)
            if form.is_valid():
                post=form.save(commit=False)
                post.status="Draft"
                base_slug = slugify(post.title)
                post.slug = f"{base_slug}-{str(uuid.uuid4())[:4]}"
                post.is_featured=False
                post.author=request.user
                post.save()
            
                messages.success(request,'Post created successfully')
                return HttpResponseRedirect(request.path)
            else:
                
                print(form.errors)
                return redirect('profile-wise-post')
        context={
            'posts':posts,
            'latest':latest,
            'number_post':number_of_post,
            'draft':draft,
            'form':form,
            'published_post':published_post
        }
        return render(request,'authentication/profile-wise-post.html',context)
    except Blog.DoesNotExist:
        form=PostForm()
        if request.method=='POST':
            form=PostForm(request.POST,request.FILES)
            if form.is_valid():
                post=form.save(commit=False)
                post.status="Draft"
                base_slug = slugify(post.title)
                post.slug = f"{base_slug}-{str(uuid.uuid4())[:4]}"
                post.is_featured=False
                post.author=request.user
                post.save()
            
                messages.success(request,'Post created successfully')
                return HttpResponseRedirect(request.path)
            else:
                
                print(form.errors)
                return redirect('profile-wise-post')
        context={
       
            'number_post':0,
            'draft':0,
            'form':form,
            'published_post':0
        }
        return render(request,'authentication/profile-wise-post.html',context)

@login_required
def edit_post_profile_wise(request,slug):
    post = get_object_or_404(Blog, slug=slug, author=request.user)
    
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            data=form.save(commit=False)
            data.author=request.user
            data.status="Draft"
            base_slug=slugify(data.title)
            data.slug=f"{base_slug}-{str(uuid.uuid4())[:4]}"
            data.save()
            return JsonResponse({'status': 'success'})
        else:
            # যদি ফর্মে কোনো ভুল থাকে (যেমন: রিকোয়ার্ড ফিল্ড খালি)
            print(form.errors) 
            return JsonResponse({'status': 'error', 'errors': form.errors.as_json()}, status=400)
            
    return JsonResponse({'status': 'error'}, status=400)


@login_required
def delete_post_profile_wise(request,slug):
    post = get_object_or_404(Blog, slug=slug, author=request.user)
    if request.method == "POST":
        post.delete()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)

@login_required
def edit_profile(request,id):
    prof=get_object_or_404(Profile,id=id)
    user=request.user
    if request.method=='POST':
        userform=UserEditForm(request.POST,instance=user)
        profileForm=ProfileEditForm(request.POST,request.FILES,instance=prof)
        if userform.is_valid() and profileForm.is_valid():
            userform.save()
            profileForm.save()
            return JsonResponse({'status':'success'})
        return JsonResponse({'status':'error'},status=400)
    return JsonResponse({'status':'error'},status=400)
    

    
@login_required
def change_password(request):
    form=ChangePaswordForm()
    if request.method=="POST":
        form=ChangePaswordForm(request.POST)
        if form.is_valid():
            pass1=form.cleaned_data['pass1']
            prev_pass=form.cleaned_data['prev_pass']
            if not check_password(prev_pass,request.user.password):
                messages.error(request,'Wrong current password')
                return redirect('change-password')
            else:
                request.user.set_password(pass1)
                request.user.save()
                update_session_auth_hash(request,request.user)
                messages.success(request,'password change successfully')
                return redirect('profile')
    else:
        form=ChangePaswordForm()
    context={
        'form':form
    }
    return render(request,'authentication/change-password.html',context)


class CustomResetPasswordView(PasswordResetView):
    template_name = 'authentication/reset-password-form.html'
    success_url = reverse_lazy('password_reset_done')
    email_template_name = 'authentication/password_reset_email.html'
    html_email_template_name = 'authentication/password_reset_email.html'
    
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        try:
            user = User.objects.get(username=username)
            if user.email:
                # ১. ডাটা কপি করা
                data = request.POST.copy()
                # ২. ইমেইল ইনজেক্ট করা
                data['email'] = user.email
                # ৩. রিকোয়েস্টের পোস্ট ডাটা আপডেট করা
                request.POST = data
           
                # এবার সুপার মেথড কল করুন
                return super().post(request, *args, **kwargs)
            else:
                messages.error(request, "ইউজারের ইমেইল পাওয়া যায়নি!")
        except User.DoesNotExist:
            messages.error(request, "এই ইউজারনেমটি ভুল!")
        
        return render(request, self.template_name)
    