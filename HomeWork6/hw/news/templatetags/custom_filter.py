from django import template


register = template.Library()

#Подвергнем цензуре слово редиска и копать

censor_list_root = ['редиск', 'редисок', 'копа']
censor_list_ending = ['а', 'и', 'е', 'у', 'ой', 'ами', 'ах', 'ю', 'ешь', 'ет', 'ем', 'ете', 'ют', 'л', 'ла', 'ли', 'ть']

@register.filter()
def bw_filter(value):
    value = value.replace('.', ' . ')
    value = value.replace(',', ' , ')
    value = value.replace('"', ' " ')
    value = value.replace("'", " ' ")
    ans = ''
    bwf = False
    try:
        for a in value.split(' '):
            for b in censor_list_root:
                for c in censor_list_ending:
                    if a.lower() == b+c:
                        bwf = True
                        lenth = len(b+c) - 1
            if bwf:
                ans+=a[0] + (lenth) * '*' + ' '
                bwf = False
            else:
                ans+=a+' '
    except TypeError:
        pass
    value = ans
    value = value.replace(' . ', '.')
    value = value.replace(' , ', ',')
    value = value.replace(' " ', '"')
    value = value.replace(" ' ", "'")
    return value

