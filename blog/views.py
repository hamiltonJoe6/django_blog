from django.shortcuts import render, get_object_or_404
from .models import Blog, Category

def index(request):
	if 'search' in request.GET:
		search = request.GET['search']

		blog = Blog.objects.filter(title__icontains=search)
	else:
		blog = Blog.objects.all()

	return render(request, 'blog/index.html', {'blogs': blog})

def indexdetail(request, slug):
	blog = get_object_or_404(Blog, slug=slug)
	latest = Blog.objects.all()[:5]
	return render(request, 'blog/detail.html', {'blog': blog, 'latest': latest})

def about(request):
	return render(request, 'blog/about.html')

def categories(request):
	category_list = Category.objects.exclude(name="default")
	context = {
		'category_list': category_list,
		}
	return context

def categoryList(request, category):
	blog = Blog.objects.filter(category__name=category)
	return render(request, 'blog/category.html', {'blogs': blog})
















