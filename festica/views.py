from django.views.generic import TemplateView
from django.shortcuts import render, redirect 
from django.views.decorators.csrf import csrf_exempt
from competitions.models import Competition
import razorpay

class TestPage(TemplateView):
    template_name = 'test.html'

class AboutPage(TemplateView):
    template_name = 'about.html'

class HomePage(TemplateView):
    template_name = 'index_2.html'


def pay_with_razor(request, pk):
    if request.method == "POST":
        amount = 5000
        
        client = razorpay.Client(
            auth=("rzp_test_VDUrLjpkd8r5Ae", "1GxLaRC53HNniiX03rxbWZO6"))
        
        client.set_app_details({"title" : "Django", "version" : "2.2"})

        payment = client.order.create({'amount': amount, 'currency': 'INR',
                                       'payment_capture': '1'})
    context = {'pk':pk}
    return render(request, 'pay_index.html', context)

@csrf_exempt
def success_payment(request, pk):
    this_competition = Competition.objects.get(pk=pk)
    this_competition.add_user_to_list_of_attendees(user=request.user)
    this_competition.decrement_seats()
    
    return render(request, "pay_success.html")