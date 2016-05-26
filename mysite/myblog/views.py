from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext, loader

from myblog.models import Post


# Create your views here.

def stub_view(request, *args, **kwargs):
    body = "Stub V!\n\n"

    body += "Args:\n"
    body += "\n".join(["\t%s" % a for a in args])

    body += "Kwargs:\n"
    body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])

    return HttpResponse(body, content_type="text/plain")
	
# def stub_view(request, *args, **kwargs):
#     body = "Stub View\n\n"
#     if args:
#         body += "Args:\n"
#         body += "\n".join(["\t%s" % a for a in args])
#     if kwargs:
#         body += "Kwargs:\n"
#         body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
#     return HttpResponse(body, content_type="text/plain")


def list_view(request):
	template = loader.get_template('list.html')
	posts = Post.objects.all()
	context = RequestContext(
		request,
		{'posts': posts},
	)
	body = template.render(context)
	return HttpResponse(body, content_type="text/html")
    #published = Post.objects.exclude(published_date__exact=None)
    #posts = published.order_by('-published_date')
    #context = {'posts': posts}
    #return render(request, 'list.html', context)


def detail_view(request, *args, **kwargs):
	post_id = Kwargs['post_id']
	
	post = Post.objects.get(pk=post_id)

	context = {'post': post}

	return render(request, 'detail_view', context)

	# published = Post.objects.exclude(published_date__exact=None)
	# try:
	# 	post = published.get(pk=post_id)
	# except Post.DoesNotExist:
	# 	raise Http404
	# context = {'post': post}
	# return render(request, 'detail.html', context)