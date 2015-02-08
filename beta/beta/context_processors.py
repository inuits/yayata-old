from django.conf import settings

def yata_version(request):
    return {'YATA_VERSION': settings.YATA_VERSION}
