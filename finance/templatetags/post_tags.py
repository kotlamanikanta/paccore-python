from django import template
from admissions.models import Student

register=template.Library()

@register.simple_tag
def total_stu():
    return Student.objects.count()
