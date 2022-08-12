from django.http import HttpResponse

from .helpers.messages import HOME_PAGE


def home_page_view(request):
    """
    This Method Return HTTP Response and Method Contain Simple Explain For Flight Tracking Application.
    :param request:
    :return:
    """
    return HttpResponse(HOME_PAGE, content_type='text/plain')
