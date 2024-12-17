from django.shortcuts import get_object_or_404, render
from myBlog import models
from myBlog.models import Post, Category
from django.views.generic import ListView, DetailView, TemplateView
from django.db.models import Q
from .forms import SearchForm
# Create your views here.



class PostList(ListView):
    model = models.Post
    context_object_name = 'posts'
    template_name = 'post_list.html'
    paginate_by = 10
    
    def get_queryset(self):
        return Post.objects.filter(status=Post.ACTIVE)
    
   
class PostDetail(DetailView):
    model = models.Post
    template_name = 'post_detail.html'
    
    def get_object_or_404(self, queryset = None):
        categoty_slug = self.kwargs.get('categiry_slug')
        slug = self.kwargs.get('slug')
        post = Post.objects.get(category__slug = categoty_slug, slug= slug)
                      
        return post
    
     # # count number of views
    def get_object(self, queryset = None):
        obj = super().get_object(queryset)
        obj.views = obj.views + 1
        obj.save()
        return obj
 
class CategoryList(ListView):
    model = models.Post
    template_name = 'category_list.html'
    context_object_name = "catposts"
    
    def get_queryset(self):
        # get() will retunr one result. To ensure code works for multiple results, use filter() instead of get()
        category = get_object_or_404(Category, slug=self.kwargs['slug'])
        q = Post.objects.filter(category = category)  
        print(q)
        return Post.objects.filter(category = category)   

class ArchiveList(ListView):
    model = models.Post
    template_name = 'archive_list.html'
    context_object_name = 'archives'
    
    def get_queryset(self):
        return Post.objects.filter(status = Post.ARCHIVE)

# FBV for search
def search(request):
    query = request.GET.get('query', '')
    posts = Post.objects.filter(Q(title__icontains=query) | Q(summary__icontains = query) | Q(content__icontains = query))
    return render(request, 'myBlog/search_list.html', {'posts':posts, 'query':query})

# CBV for search 

class SearchList(ListView):
    model = Post
    template_name = 'search_list.html'
    
    def get_queryset(self):
        # queryset = super().get_queryset()
        queryset = Post.objects.none()
        query = self.request.GET.get('query', '') 
        # 'query' in request.GET is the name of the search field in the template 
        if query:
            queryset = Post.objects.filter(Q(title__icontains=query) | Q(summary__icontains = query) | Q(content__icontains = query))
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('query', '')
        return context
    # query results will be available in the template as 'object_list'