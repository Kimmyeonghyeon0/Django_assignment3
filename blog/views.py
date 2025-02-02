from django.shortcuts import render, get_object_or_404

from blog.models import Blog

def blog_list(request):
    blog = Blog.objects.all()

    visits = int(request.COOKIES.get('visits', 0)) + 1

    request.session['count'] = request.session.get('count', 0) + 1

    context = {
        'blog': blog,
        'count': request.session['count'],
    }

    response = render(request, 'blog_list.html', context)

    response.set_cookie('visits', visits)
    return response


def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    context = {'blog': blog}
    return render(request, 'blog_detail.html', context)