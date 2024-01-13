from django.shortcuts import render
from core.forms import StatusFormSet

from core.models import Order

# Create your views here.


def order(request):
    order = Order.objects.all()
    if request.method == "POST":
        print(request.POST)

        order_instance = Order.objects.filter(id=request.POST["id"]).first()
        order_instance.status = request.POST["status"]
        order_instance.save()
    return render(request, "index.html", context={"orders": order})
