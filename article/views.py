from django.shortcuts import render, get_object_or_404
from .forms import CommentForm
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.core.paginator import Paginator
from article.models import Article_Info
from .filters import articleFilter

# Create your views here.


def articles(request):
    art_list = Article_Info.objects.all()

    myfilter = articleFilter(request.GET, queryset=art_list)
    art_list = myfilter.qs

    paginator = Paginator(art_list, 8)
    page_num = request.GET.get('page')
    articles = paginator.get_page(page_num)
    context = {
        'count': paginator.count,
        'articles': articles,
        'title': 'Articles',
        'myfilter': myfilter,
    }
    return render(request, "article/article.html", context)


def single_article(request, slug):
    post = get_object_or_404(Article_Info, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None

    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    context_single = {'art': Article_Info.objects.get(slug=slug),
                      'title': Article_Info.objects.get(slug=slug),
                      'post': post,
                      'comments': comments,
                      'new_comment': new_comment,
                      'comment_form': comment_form}

    return render(request, "article/single_article.html", context_single)
