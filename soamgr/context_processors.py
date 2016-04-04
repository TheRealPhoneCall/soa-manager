import soaprj.settings as settings


def extra(request):
    return {
        'VERSION': settings.VERSION,
    }
