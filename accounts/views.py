from django.views.generic import TemplateView

class ConfirmAccountComplete(TemplateView):
    template_name = "email_confirmation_complete.html"
