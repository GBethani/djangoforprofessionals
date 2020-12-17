import stripe
from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.models import Permission
from django.views.generic.base import TemplateView
# Create your views here.
stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

class OrderPageView(TemplateView):
    template_name = 'orders/purchase.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['stripe_key'] = settings.STRIPE_TEST_PUBLISHABLE_KEY
        return context

def charge(request):
    permission = Permission.objects.get(codename='special_status')
    current_user = request.user
    current_user.user_permissions.add(permission)
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=3900,
            currency='inr',
            description='Purchase all books',
            source=request.POST['stripeToken']
        )
    return render(request,'orders/charge.html')