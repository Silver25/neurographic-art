from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post

# Create your views here.

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

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "journal/post_detail.html",
        {"post": post},
    )