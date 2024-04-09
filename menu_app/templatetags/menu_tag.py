from django import template
from menu_app.models import MenuItem

register = template.Library()


@register.inclusion_tag('menu.html')
def draw_menu(menu_name, request):
    menu_items = MenuItem.objects.filter(parent__isnull=True, title=menu_name)
    return {
        'menu_items': menu_items,
        'current_url': request.build_absolute_uri()
    }
