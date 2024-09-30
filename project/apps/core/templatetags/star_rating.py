# templatetags/star_rating.py
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def rating(rating, total=5, font_size = 12):
    full_star = f'''
    <svg width="{font_size}" height="{font_size}" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M4.2935 4.11797L5.5925 1.50197C5.63031 1.42626 5.68847 1.36259 5.76044 1.31808C5.83242 1.27357 5.91537 1.25 6 1.25C6.08462 1.25 6.16757 1.27357 6.23955 1.31808C6.31153 1.36259 6.36968 1.42626 6.4075 1.50197L7.7065 4.11797L10.6105 4.53997C10.6943 4.55159 10.7731 4.58652 10.8379 4.64078C10.9028 4.69504 10.9511 4.76644 10.9773 4.84683C11.0035 4.92723 11.0066 5.01338 10.9862 5.09545C10.9659 5.17752 10.9228 5.2522 10.862 5.31097L8.761 7.34597L9.257 10.221C9.3205 10.59 8.9305 10.871 8.597 10.697L6 9.33897L3.4025 10.697C3.0695 10.8715 2.6795 10.59 2.743 10.2205L3.239 7.34547L1.138 5.31047C1.07749 5.25166 1.0347 5.17705 1.01448 5.09513C0.994262 5.01321 0.997433 4.92725 1.02363 4.84704C1.04983 4.76683 1.09801 4.69558 1.16268 4.64139C1.22736 4.58719 1.30594 4.55223 1.3895 4.54047L4.2935 4.11797Z" fill="#FFCC00" stroke="#FFCC00" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
    '''
    
    empty_star = f'''
    <svg width="{font_size}" height="{font_size}" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M4.2935 4.11797L5.5925 1.50197C5.63031 1.42626 5.68847 1.36259 5.76045 1.31808C5.83242 1.27357 5.91538 1.25 6 1.25C6.08463 1.25 6.16758 1.27357 6.23956 1.31808C6.31153 1.36259 6.36969 1.42626 6.4075 1.50197L7.7065 4.11797L10.6105 4.53997C10.6943 4.55159 10.7731 4.58652 10.8379 4.64078C10.9028 4.69504 10.9511 4.76644 10.9773 4.84683C11.0035 4.92723 11.0066 5.01338 10.9862 5.09545C10.9659 5.17752 10.9228 5.2522 10.862 5.31097L8.761 7.34597L9.257 10.221C9.3205 10.59 8.9305 10.871 8.597 10.697L6 9.33897L3.4025 10.697C3.0695 10.8715 2.6795 10.59 2.743 10.2205L3.239 7.34547L1.138 5.31047C1.07749 5.25166 1.0347 5.17705 1.01448 5.09513C0.994266 5.01321 0.997437 4.92725 1.02364 4.84704C1.04983 4.76683 1.09801 4.69558 1.16269 4.64139C1.22736 4.58719 1.30594 4.55223 1.3895 4.54047L4.2935 4.11797Z" stroke="#FFCC00" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
    '''

    stars = full_star * rating + empty_star * (total - rating)
    return mark_safe(stars)  # Mark the output as safe
