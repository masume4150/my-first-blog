from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from .forms import AboutUsForm
# Create your views here.


def index(request):
    context = {}
    return render(request, "/templates/food/index.html", context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def useraccount(request):
    form = AboutUsForm()
    return render(request, 'account/aboutUs.html', {'form': form})
