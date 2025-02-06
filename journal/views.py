from django.shortcuts import render, get_object_or_404
# Generic View for the function to create PostList
from django.views import generic
from .models import Post
from .forms import CommentForm

# Create your views here.
# Post (with a capital P) always refers to the 'Post' model in model.py created. 
# On the other hand, 'post' (with a lowercase p) refers to an individual blog post
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-created")
    template_name = "journal/index.html"
    paginate_by = 6

def post_detail(request, slug):
    """
    Display an individual :model:`journal.Post`.

    **Context**

    ``post``
        An instance of :model:`journal.Post`.

    **Template:**

    :template:`journal/post_detail.html`
    """
    # pull only Published posts from db - models.py-STATUS=1
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)  # get data or raise a Http404 error
    comments = post.comments.all().order_by("-created")
    comment_count = post.comments.filter(approved=True).count()
    comment_form = CommentForm()

    # helper function
    return render(
        request,
        "journal/post_detail.html",  # path to the template file
        {
            "post": post,  # set the name of the object
            "comments": comments,
            "comment_count": comment_count,  # set the number of the comments
            "comment_form": comment_form,
         }
    )
    # context ("post") is how we pass data from our views to our templates
    # context is a Python dictionary of key/value pairs that is sent to the template
    # It is convention that the key name would be the same as the variable name