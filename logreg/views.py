from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import users, articles, comments, likes
from .backends import UserBackend
from .forms import UserRegisterForm, UserLoginForm, ArticleRegisterForm
from django.contrib import messages
from django.contrib.auth import logout, login
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
# Create your views here.

#login method
def logindex(request):
    #if loged in user tries to access login redirect
    if request.user.is_authenticated:
        return redirect('../profile')
    # if POST get fields
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        #if valid authenticate through custom model
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = UserBackend.authenticate(request, username=username, password=password)
            if user is not None:
                if user == 'Wrong user or password':
                    messages.error(request, 'Wrong user or password')
                    return redirect('/logreg/login/')
                elif user == 'User does not exist':
                    messages.error(request, 'User does not exist')
                    return redirect('/logreg/login/')
                elif user == 'User blocked':
                    messages.error(request, 'User blocked')
                    return redirect('/logreg/login/')
                else:
                    messages.success(request, 'Welcome ' + user.username)
                    login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                    return HttpResponseRedirect('../profile')
            else:
                messages.error(request, 'User does not exist')
                return redirect('/logreg/login/')
        else:
            messages.error(request, form.errors)
            return redirect("/logreg/login/")
    else:
        form = UserLoginForm()
        return render(request, 'logreg/login.html', {'form': form})

#register method
def regindex(request):
    if request.user.is_authenticated:
        return redirect('../profile')
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # get all field. check if email exists (user is done automatically)
            username = form.cleaned_data['username']
            password = make_password(form.cleaned_data['password1'])
            email = form.cleaned_data['email']
            try:
                check = users.objects.get(email=email)
                messages.success(request, "User exists")
                return redirect("/logreg/register")
            except:
                pass
            dob = form.cleaned_data['Date_of_birth']
            phone = form.cleaned_data['phone']
            music = form.cleaned_data['music']
            games = form.cleaned_data['games']
            arts = form.cleaned_data['arts']
            movies = form.cleaned_data['movies']
            bio = form.cleaned_data['bio']
            interests = ''
            if music: interests += ('Music/')
            if games: interests += ('Games/')
            if arts: interests += ('Arts/')
            if movies: interests += ('Movies/')

            # insert new user in auth users
            user = User(username=username, email=email)
            # is not stuff or superuser. only admin can change this
            user.is_staff = False
            user.is_superuser = False
            user.save()

            #create new user in users
            new_user = users(id=User.objects.get(username=username).id, username=username, email=email, password=password, dob=dob, phone=phone, interests=interests[:-1], bio=bio)
            new_user.save()

            messages.success(request, "User: " + username + " registered successfully !")
            return redirect("/")
        else:
            messages.error(request, form.errors)
            return redirect("/logreg/register/")
    else:
        form = UserRegisterForm()
        return render(request, 'logreg/register.html', {'form': form})

#profile method
def profile(request):
    if request.user.is_authenticated:
        #get data and posts of loged in user. pass it as input to html
        data = users.objects.get(username=request.user.username)
        posts = articles.objects.all().filter(user_id=request.user.id)
        return render(request, 'profile/profile.html', {'data' : data, 'posts':posts})
    else:
        messages.error(request, 'You have to be logged in for this action !')
        return HttpResponseRedirect('/logreg/login/')

#feed method
def feed(request):
    if request.user.is_authenticated:
        #pass all posts as input
        posts = articles.objects.all()
        posters = []
        # get poster name
        for post in posts:
            # get poster name
            post.user_id = User.objects.get(id=post.user_id).username
        return render(request, 'article/feed.html', {'posts': posts})
    else:
        messages.error(request, 'You have to be logged in for this action !')
        return HttpResponseRedirect('/logreg/login/')

#create article method
def regart(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ArticleRegisterForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                details = form.cleaned_data['details']
                music = form.cleaned_data['music']
                games = form.cleaned_data['games']
                arts = form.cleaned_data['arts']
                movies = form.cleaned_data['movies']
                categories = ''
                if music: categories += ('Music/')
                if games: categories += ('Games/')
                if arts: categories += ('Arts/')
                if movies: categories += ('Movies/')
                article = articles(title=title, details=details, category=categories, likesNo=0, commentsNo=0, user_id=request.user.id)
                article.save()
                messages.success(request, "Post: " + title + " posted successfully !")
                return HttpResponseRedirect('../profile/')
        else:
            form = ArticleRegisterForm()
            return render(request, 'article/regart.html', {'form':form})
    else:
        messages.error(request, 'You have to be logged in for this action !')
        return HttpResponseRedirect('/logreg/login/')

#view article methdo
def seeart(request, aid):
    if request.user.is_authenticated:
        #get article selected
        post = articles.objects.get(aid=aid)
        #get poster name
        poster = User.objects.get(id=post.user_id)
        #update likes and comments number for safety
        liked = likes.objects.all().filter(aid_id=aid)
        likesNo = len(liked)
        commented = comments.objects.all().filter(aid_id=aid)
        commentsNo = len(commented)
        post.likesNo = likesNo
        post.commentsNo = commentsNo
        post.save()
        #build comments -> ('comment_username: comment_test')
        coms = []
        for comment in commented:
            coms.append(User.objects.get(id=comment.uid_id).username + ': ' + comment.comment)
        #if logged in user already likes the article
        #liked button becomes dislike button
        try:
            u_like = likes.objects.get(aid_id=aid, uid_id=request.user.id)
            u_like = True
        except:
            u_like = False
        #ignore froom (placeholder)
        froom = 'feed'
        return render(request, 'article/seeart.html', {'poster': poster, 'post': post, 'liked': len(liked), 'coms': coms, 'u_like': u_like, 'froom':froom})
    else:
        messages.error(request, 'You have to be logged in for this action !')
        return HttpResponseRedirect('/logreg/login/')

#post comment method
def compost(request, aid, uid):
    if request.user.is_authenticated:
        #get comment and insert to database
        ucom = request.POST.get('comment')
        newcom = comments(comment=ucom, aid_id=aid, uid_id=uid)
        newcom.save()
        #update article comment number
        article = articles.objects.get(aid=aid)
        article.commentsNo += 1
        article.save()
        return HttpResponseRedirect('/logreg/seeart/'+str(aid))
    else:
        messages.error(request, 'You have to be logged in for this action !')
        return HttpResponseRedirect('/logreg/login/')

#like method
def like(request, aid, uid):
    if request.user.is_authenticated:
        #insert like log to database
        lik = likes(aid_id=aid, uid_id=uid)
        lik.save()
        article = articles.objects.get(aid=aid)
        article.likesNo += 1
        article.save()
        return HttpResponseRedirect('/logreg/seeart/'+str(aid))
    else:
        messages.error(request, 'You have to be logged in for this action !')
        return HttpResponseRedirect('/logreg/login/')

#dislike method
def dislike(request, aid, uid):
    if request.user.is_authenticated:
        #update dislike log in database
        article = articles.objects.get(aid=aid)
        article.likesNo -= 1
        article.save()
        lik = likes.objects.get(aid_id=aid, uid_id=uid)
        lik.delete()
        return HttpResponseRedirect('/logreg/seeart/'+str(aid))
    else:
        messages.error(request, 'You have to be logged in for this action !')
        return HttpResponseRedirect('/logreg/login/')

#ousting
def oust(request):
    #oust
    logout(request)
    return HttpResponseRedirect('/')

#kicking
def kick(request):
    #kick
    if request.user.is_authenticated:
        return render(request, 'profile/profile.html')
    else:
        messages.error(request, 'You have to be logged in for this action !')
        return HttpResponseRedirect('/logreg/login/')

#delete account method
def delete(request):
    #diplay confirmation form
    if request.user.is_authenticated:
        return render(request, 'logreg/delete.html')
    else:
        messages.error(request, 'You have to be logged in for this action !')
        return HttpResponseRedirect('/logreg/login/')

#delete action
def delete_account(request):
    if request.user.is_authenticated:
        #delete user from users and auth users
        user = users.objects.get(id=request.user.id)
        auth_user = User.objects.get(id=request.user.id)
        user.delete()
        auth_user.delete()
        messages.success(request, "Account deleted successfully")
        return redirect('/')
    else:
        messages.error(request, 'You have to be logged in for this action !')
        return HttpResponseRedirect('/logreg/login/')
