from core.models import Setting

def website_settings(request):
    return {
        'setting': Setting.objects.first()
        }