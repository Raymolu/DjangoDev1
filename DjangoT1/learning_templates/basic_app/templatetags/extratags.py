from django import template

register = template.Library()


def cutit(value, arg):
    return value.replace(arg,'')

register.filter('cutit',cutit)
