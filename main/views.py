from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from .models import UserComments, TopicCategory, UserProfile
from .forms import NewUserForm, EditProfileForm, EditProfilePicture, PostCreateForm
from .forms import AddingCommentsForm
from django.views.generic import TemplateView
from django.template import RequestContext
from django.shortcuts import get_object_or_404


def homepage(request):
    return render(request, "main/home.html",
                    {"comments": UserComments.objects.all, "category": TopicCategory.objects.all,
                    'comment_list': TopicCategory.objects.all()})


# def add_comment_to_post(request, pk):
#     category = TopicCategory.objects.get(pk = pk)
#     related_category = TopicCategory.objects.filter(tags = category.tags).exclude(pk=category.pk)[:4]
#     comment = related_category.cleaned_data['product']
#     category = related_category.cleaned_data['category']
#     context = AddingCommentsForm()
#     if request.method == 'POST':
#         form = AddingCommentsForm(request.POST)
#         if form.is_valid():
#             comment = form.cleaned_data['user_comments']
#             category.comments_set.create(comment=comment)
#     return redirect(request, 'main:homepage', context)



def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("main:homepage")

        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request=request,
                          template_name="main/register.html",
                          context={"form": form})

    form = NewUserForm
    return render(request=request,
                  template_name="main/register.html",
                  context={"form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect("main:homepage")
            else:
                messages.error(request, "Invalid username or password!")
        messages.error(request, "Invalid username or password!")

    form = AuthenticationForm()
    return render(request,
                  "main/login.html",
                  {"form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully")
    return redirect("main:homepage")


def edit(request):
    user_profile = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        update_profile_form = EditProfilePicture(data=request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            profile = update_profile_form.save(commit=False)
            profile.profile_image = request.FILES['profile_image']
            messages.info(request, f"You have successfully updated your profile")
            profile.save()
            return redirect("main:homepage")
        else:
            form = EditProfileForm(instance=request.user)
            return render(request=request,
                          template_name="main/edit.html",
                          context={"form": form})
    else:
        form = EditProfileForm(instance=request.user)
        update_profile_form = EditProfilePicture(instance=user_profile)
        return render(request=request,
                      template_name="main/edit.html",
                      context={"form": form, "update_profile_form":update_profile_form})


def post_create(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
    else:
        form = PostCreateForm()
    context = {
        'form':form,
    }
    return render(request, 'main/post_create.html', context)




