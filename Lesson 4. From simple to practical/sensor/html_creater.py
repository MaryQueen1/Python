from user_interface import temperature_view
from user_interface import wind_speed_view
from user_interface import preassure_view

def create(device=1):
    style = 'style="font-size:22px;"'
    html='<html>\n <head></head>\n <body>\n'
    html+='<p{}>Temperature:{} c</p>\n'\
        .format(style,temperature_view(device))
    html+='<p{}>Wind_speed:{} m/s</p>\n'\
        .format(style,wind_speed_view(device))
    html+='<p{}>Preassure:{} c</p>\n'\
        .format(style,preassure_view(device))

    with open('index.html','w') as page:
        page.write(html)

    return html

def new_create(data,device=1):
    t,p,w = data
    style = 'style="font-size:22px;"'
    html='<html>\n <head></head>\n <body>\n'
    html+='<p{}>Temperature:{} c</p>\n'\
        .format(style,t)
    html+='<p{}>Wind_speed:{} m/s</p>\n'\
        .format(style,w)
    html+='<p{}>Preassure:{} c</p>\n'\
        .format(style,p)

    with open('inew_ndex.html','w') as page:
        page.write(html)

    return data