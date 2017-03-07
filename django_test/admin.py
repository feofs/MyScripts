''''
Кажется это должна быть адмика
Так называется веб-интерфейс, доступный только
уполномоченным администраторам сайта и позволяющий добавлять,
редактировать и удалять содержимое сайта.
Административный интерфейс - там где можно добавлять записи, статьи, товары, модерировать сообщения пользователей и все такое
Но его программить скучно, т.к все похожи друг на друга

Нужно аутентифицировать пользователей, отображать формы и обрабатывать отправленные с их помощью данные, проверять введенные данные и т. д.
Утомительная, повторяющаяся работа. А как фреймворк Django подходит к утомительной, повторяющейся работе? Он делает ее за вас – всего в паре строчек кода. Раз вы пользуетесь
Django, можете считать, что задача написания административного интерфейса уже решена.

Джанго сам создает автоматически административные интерфейсы на основе модели.
Для этого Джанго считывает метаданные из модели и создает интерфейсы администратора

Автоматическая админка - часть более широкого набора приложений, именуемого django.contrib.
В него входят разнообразные полезные дополнения к ядру каркаса

То есть django.contrib - типа стандартной библиотеки питона
Административный интерфейс – первый пакет из комплекта django.
contrib, рассматриваемый в этой книге; строго говоря, он называется
django.contrib.admin.

В него входят еще
django.contrib.auth - система аутентификации пользователей
django.contrib.sessions - поддержка анонимных сеансов
django.contrib.commits - система замечаний пользователей

Для активации нужно в INSTALLED_APPS
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
и в классы MIDDLEWARE

'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware'

А также сделать суперпользователя
python manage.py createsuperuser и раскоментить или добавить в УРЛы
from django.contrib import admin
admin.autodiscover()
# И этот шаблонURL...
urlpatterns = patterns(‘’,
    # ...
    (r’^admin/’, include(admin.site.urls)),
    # ...
    )

Затем
python.exe manage.py makemigrations auth
python.exe manage.py makemigrations sessions
python.exe manage.py migrate auth
python.exe manage.py migrate sessions
python.exe manage.py createsuperuser
http://127.0.0.1:8000/admin/.

Так как не активированна ни одна модель, то список пуст, только Пользователи и Группы
С каждым типом данных в административном интерфейсе Django свя-
зан список для изменения и форма редактирования. В списке для из-
менения показаны все имеющиеся в базе данных объекты данного типа,
а форма редактирования позволяет добавлять, изменять и удалять кон-
кретные записи.

Чтобы узнать поддерживает ли админка родной язык нужно
‘django.middleware.locale.LocaleMiddleware’ в па-
раметр MIDDLEWARE_CLASSES после строчки ‘django.contrib.sessions.
middleware.SessionMiddleware’.

Щелкните на ссылке Change (Изменить) в строке Users (Пользователи),
чтобы загрузить страницу со списком для изменения (рис. 6.3).
На этой странице отображаются все имеющиеся в базе данных пользо-
ватели; можете считать, что это облагороженный для веб аналог SQL-
запроса SELECT * FROM auth_user.

При редактировании об

ага и вот теперь мы можем включить наши модели определяющие классы для начала их нужно импортировать
так
from mysite.books.models import Publisher, Author, Book
777-888-999
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book)
'''

from django.contrib import admin

# Register your models here.
from mysite.books.models import Publisher, Author, Book

admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book)