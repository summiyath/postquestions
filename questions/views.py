from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from questions.forms import PostForm, AnswerForm
from questions.models import Post, Answer, Like


# Create your views here.
def home(request):
    obj = Post.objects.all()
    return render(request, 'index.html', {'obj': obj})

@login_required(login_url ='login')
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            Post = form.save(commit=False)
            Post.author = request.user
            form.save()
            return redirect('/')
    else:
        form = PostForm()
        return render(request, 'create_post.html', {'form': form})


def post_answers(request, id):
    ans = Answer.objects.filter(post_id=id)
    nums = Post.objects.get(id =id)


    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            value = form.save(commit=False)
            value.user = request.user

            value.post = nums
            form.save()
        return redirect('/')
    else:
        form = AnswerForm()

    return render(request,'answers.html',{'ans':ans,'form':form})
def like_answer(request, id):
    print("Function called")

    answer = Answer.objects.get(id=id)



    if request.method =='POST':
        print("abn bs")

        obj = Like.objects.filter(answer=answer,user=request.user)
        if obj:
            obj.delete()



        else:
            val =Like.objects.create(answer = answer,user =request.user)
            val.save()
    count = Like.objects.filter(answer=answer).count()
    print("count",count)
    return render(request,'answers_detail.html',{'count':count,'answer':answer})




