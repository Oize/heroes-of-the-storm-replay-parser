from django import template

register = template.Library()

#@register.filter('break')
#def break_(loop):
#    raise StopLoopException(loop, False)
    
@register.filter('getname')
def lower_(value):
    return value.lower().replace(' ', '').replace('.', '').replace("'", '')
    
@register.filter('getherourl')
def geturl(heroname):
    return 'images/heroes/' + str(heroname) + '.jpg'
