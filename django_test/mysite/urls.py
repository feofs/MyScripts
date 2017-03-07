"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import sys
sys.path.append('C:\\MyScripts\\django_test\\mysite\\books')

from django.conf.urls import url
from django.contrib import admin
from django_test.mysite.books.views import *
from django_test.mysite.mysite.views import *

print(sys.path)
#Джанго удаляет символ слеша в начале с люого поступающего УРЛа и только потом начинает соспоставление с шаблонами, поэтому и шаюлон сопоставление с /hello/ выглядит не так очевидно
#если убрать $ в конце выражения, то ему будут соотсвествовать и hello/foo и hello/bar и все остальное, а это не то чего бы нам хотелось, поэтому
#Аналогично, если бы мы опустили знак вставки в начале (например, ‘hello/$’), то ему соответствовал бы любой URL, заканчивающийся строкой hello/, например, /foo/bar/hello/.
#Если УРЛ будет без слеша, то механизм Джанго автоматически вызовет для него обработчик но соответсвующий со слэшем,
#если же нам нравяьтся больше адресса не завершенные слешем то нужно установить переменную APPEND_SLASH=False
#тут функции как видно вызываются без какой либо передачи переменных, туда по умолчанию передается request

#Корень сайта у нас не описан, и если обратиться к корню сайта т.е localhost:8000 то ничего не выведет, т.к корень
#Как Джанго обрабатівает запрос - поступил УРЛ, он читает файл settings.conf и в нем ест строка ROOT_URLCONF = ‘mysite.urls’, которая указывает на то где храняться конфигурация УРЛов в данном случае в каком файле
#там находит нужный URL в списке если нет сос лешем то добавит и найдет со слешем и вызовет указанную фукнцию из указанного файла передав ей объект запроса HTTPRequest
'''
Итак за 50 страниц мы выяснили что
1)Поступает запрос к URL /hello/
2) Сервер в settings.conf ищет где хранять наша база ( в каком файле) с нашими выражениями и соответсвующей функцией которая обрабатывает url
3) Серваер просматривает найденные соответсвия, и е если мы писали без слеша добавит слеш и сопоставит с функцией
Если вы предпочитаете завершать все URL-адреса символом слеша
(как большинство разработчиков Django), то просто включайте за-
вершающий символ слеша в конец каждого шаблона
URL и не изме-
няйте принятое по умолчанию значение True параметра APPEND_SLASH.
Если же вам больше нравятся URL-адреса, не завершающиеся сим-
волом слеша, или если вы решаете этот вопрос для каждого URL
в отдельности, то задайте для параметра APPEND_SLASH

4)Если найденно соотвесвие то вызывается соответсвующая ассоицированная функция и передается 1 параметры HttpRequest
5) Функция возвращает объект HttpRespose а джанго уже возвращает ее клиенту
'''
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$',hello),
    #Конкретная временная зона указывается в файле settings.py, чтобы выводилось время для нашего часового пояса, там же есть ссылка на список актуальных часовых поясов
    url(r'^current_date/$', current_date),
    url(r'^date/$', print_date6),
    url(r'^current_section/$', current_section),
    #кароч любая группа сохранения, та что в круглых скобках всегда будет передавать это вторым, третьим и т.д параметром (после HTTPRequest) как это параметр мы в функции обзавем или в объекте не важно
    url(r'^hours/plus/(\d{1,2})/$', hours_ahead),
    url(r'^words/(\w+)/(\w+)/$', you_input),
    url(r'^books/author/(\w+)/$', show_authors)
    #url(r'^words/pattern.html$', 'pattern.hmtl')
]

