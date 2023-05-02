from django.shortcuts import render,get_object_or_404,redirect
#html 파일을 브라우저에게 돌려주기 위해 render 함수 불러오기
#존재하지 않는 객체를 요청하면 404에러창을 띄우는 get_object_or_404 함수 불러오기
from .models import Blog       #model에 저장된 Blog 데이터를 가져옴
from django.utils import timezone
from .forms import Blogform

# Create your views here.
def home(request):
    blogs=Blog.objects      #Blog 데이터들을 객체 형태로 blogs 변수에 넣어줌
    return render(request,'home.html',{'blogs':blogs})

#detail 페이지 만들기 
def detail(request, blog_id):
    blog_detail=get_object_or_404(Blog,pk=blog_id)
    return render(request,'detail.html',{'blog':blog_detail})      

#장고가 제공하는 ModelForm(forms.py) 사용하기 전... 
#def new(request):
#   return render(request,'new.html')

def new(request):
    form=Blogform()
    return render(request, 'new.html',{'form':form})

'''
form 사용 전..
def create(request):
    new_blog=Blog()
    new_blog.title=request.POST['title']
    new_blog.body=request.POST['body']
    new_blog.date=timezone.now()
    new_blog.save()
    return redirect('home')
'''

def create(request):
    form=Blogform(request.POST, request.FILES)
    if form.is_valid():
        new_blog=form.save(commit=False)
        new_blog.date=timezone.now()
        new_blog.save()
        return redirect('detail',new_blog.id)
    return redirect('home')

def delete(request, blog_id):
    blog_delete=get_object_or_404(Blog, pk=blog_id)
    blog_delete.delete()
    return redirect('home')

def update_page(request, blog_id):
    blog_update=get_object_or_404(Blog,pk=blog_id)
    return render(request, 'update.html',{'blog':blog_update})

def update(request, blog_id):
    blog_update=get_object_or_404(Blog,pk=blog_id)
    blog_update.title=request.POST['title']
    blog_update.body=request.POST['body']
    blog_update.save()
    return redirect('home')