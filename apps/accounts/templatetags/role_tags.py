from django import template

register = template.Library()


@register.filter
def has_role(user, role_code):

    if not user.is_authenticated:
        return False

    return user.has_role(role_code)