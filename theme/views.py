from django.shortcuts import render
from django.template.loader import get_template
from django.http import (HttpResponse, HttpResponseServerError,
                         HttpResponseNotFound)
from django.views.decorators.csrf import requires_csrf_token
from django.conf import settings

'''
@requires_csrf_token
def page_not_found(request, template_name="errors/404.html"):
    """
    Mimics Django's 404 handler but with a different template path.
    """
    context = {
        "STATIC_URL": settings.STATIC_URL,
        "request_path": request.path,
    }
    t = get_template(template_name)
    return HttpResponseNotFound(t.render(context, request))


@requires_csrf_token
def server_error(request, template_name="errors/500.html"):
    """
    Mimics Django's error handler but adds ``STATIC_URL`` to the
    context.
    """
    context = {"STATIC_URL": settings.STATIC_URL}
    t = get_template(template_name)
    return HttpResponseServerError(t.render(context, request))
'''