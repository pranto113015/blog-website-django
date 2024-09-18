from django.shortcuts import render,redirect
from .models import Article,TrendingPost,About
from .forms import ContactForm
# Create your views here.
# index/home section function
def home(request):
     article= Article.objects.all()
     trendingpost= TrendingPost.objects.all()
     return render(request, "index.html",{'article':article,'trendingpost':trendingpost})

def about(request):
    about = About.objects.get()
    return render(request, "about.html",{'about':about})

def blogdetails(request,pk):
   blogdetails= Article.objects.get(pk=pk)
   return render(request, "blogdetails.html",{'blogdetails':blogdetails})

def contact(request):
    form = ContactForm(request.POST)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    
    return render(request, "contact.html", {'form':form})