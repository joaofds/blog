from django.views.generic import ListView
from blog.models import Post

class PostListView(ListView):
    model = Post
    template_name = "post/post.html"
    context_object_name = "posts"