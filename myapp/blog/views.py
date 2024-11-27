from sys import stdout
from colorama import Style
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
import logging
from django.urls import reverse
from .models import post,AboutUS,chatbot
from django.core.paginator import Paginator
from .forms import ContactForm 
# Create your views here.
# static demo data
# posts=(
#     {'id':1,'post':'post1','content':'content1'},
#     {'id':2,'post':'post2','content':'content2'},
#     {'id':3,'post':'post3','content':'content3'},
#     {'id':4,'post':'post4','content':'content4'},
# )

def model(request):
    return HttpResponse("model page is here")
#redirect 
def old_url(request):
    return redirect(reverse("blog:new_url"))
def new_url(request):
    return HttpResponse("here is the new urls")
#return httml

def index(request):
    # Getting data from post model
    posts= post.objects.all()

    #paginatep
    paginator=Paginator(posts,5)
    page_number = request.GET.get('page')
    page_obj=paginator.get_page(page_number)

    return render(request,'index.html',{'page_obj':page_obj})



def detail(request,slug):
    #static data
    #post=next((item for item in posts if item['id'] == int(post_id)),None)

#geting data from model by id
   try:
    Post=post.objects.get(slug=slug) 
    
    related_posts=post.objects.filter(category=Post.category).exclude(pk=Post.id)
    # logger=logging.getLogger("TESTING")
    # logger.debug(f'post variable is {Post}')  
    return render(request,"details.html",{'post':Post,"related_posts":related_posts})
   except post.DoesNotExist:
    raise Http404("post id doen't exist")
    
    # logger=logging.getLogger("TESTING")
    # logger.debug(f'post variable is {Post}')  

def contact(request): 
   logger=logging.getLogger("TESTING")
   if request.method=='POST':
    form=ContactForm(request.POST)
    name=request.POST.get('name')
    email=request.POST.get('email')
    message=request.POST.get('message')
    success_msg="Your form is submited successfully"
    if form.is_valid():
        
       
        logger.debug(f'post data is {form.cleaned_data["name"]} {form.cleaned_data["email"]} {form.cleaned_data["message"]}') 
        return render(request,'contact.html',{'success_msg':success_msg}) 
    else :
        logger.debug('Form validation is failed')    
        return render(request,"contact.html",{'form':form,'name':name,'email':email,'message':message})
   return render(request,"contact.html")

def about(request):
   about_content=AboutUS.objects.first().content
   return render(request,'about.html',{'about_content':about_content})

def chatbot_link(request):
    chatbot_query=chatbot.objects.first().Query
    chatbot_response=chatbot.objects.first().Response
    
    return render(request,"chatbot/chatbot.html",{'chatbot_query':chatbot_query,'chatbot_response':chatbot_response})
