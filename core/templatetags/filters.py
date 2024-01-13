from django import template
from django.db.models import Count
from django.utils.safestring import mark_safe
from ..models import Order
from ..forms import StatusFormSet

register = template.Library()


# @register.simple_tag(name='total_post')
# def total_post():
#     return Post.published.count()


@register.inclusion_tag("update_order.html")
def show_latest_posts(order):
    form = StatusFormSet(instance=order)
    return {"order": order, "form": form}
