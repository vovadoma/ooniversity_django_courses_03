from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from feedbacks.models import Feedback


class FeedbackView(CreateView):
    model = Feedback
    success_url = reverse_lazy('feedback')
    template_name = 'feedbacks/feedback.html'

    def form_valid(self, form):
        feedback = form.save()
        send_mail(feedback.subject, feedback.message, feedback.from_email, settings.ADMINS, fail_silently=False)
        messages.success(self.request, 'Thank you for your feedback! We will keep in touch with you very soon!')
        return super(FeedbackView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        data = super(FeedbackView, self).get_context_data(**kwargs)
        data['title'] = 'Feedback'
        return data