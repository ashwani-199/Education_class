from django.views import generic
from django.db.models import Q
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog_list.html'
    paginate_by = 6 
    
    # This sends the 'blog' variable to your template
    extra_context = {'blog': 'active'} 

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            # Searches both the Title AND the Content of your tutorials
            return Post.objects.filter(
                Q(title__icontains=query) | Q(content__icontains=query),
                status=1
            ).distinct()
        return Post.objects.filter(status=1).order_by('-created_on')

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog_detail.html'
    
    # Ensures the Blog menu stays active even when reading a specific post
    extra_context = {'blog': 'active'}