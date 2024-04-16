
from plyer import notification

if __name__=="__main__":
    notification.notify(title='Uyarı',message= 'Bu bir denemedir.',app_name='Yılmaz App', app_icon='YılmazLogo.ico',timeout=2 )

"""
Standart Kullanım:
notify(title='', message='', app_name='', app_icon='', timeout=10, ticker='', toast=False, hints={})
"""















