#library
- Установить виртуальное окружение
- Скачать https://github.com/NatalyaKirsanova/Skillfactory_D6_library.git
- установить зависимости pip install -r requirements.txt
- запустить локальный сервер python manage.py runserver
- библиотека откроется http://localhost:8000
- вход в admin log: mi pass:1 
- /---------------------------------
1. Добавьте CSS-стили, которые вы раздаёте через STATIC для страниц библиотеки.
- стили добавлены на страницу Читатели. http://127.0.0.1:8000/readers/
2. Создайте базовый шаблон base.html и задайте в нём блоки, которые вы переопределяете в дочерних шаблонах библиотек.
- добавлен базовый шаблон base.html который дополняется шаблоном readers.html
3. Добавьте в модель книги возможность загружать картинки к книгам (в этом задании допускается сделать это через панель администратора).
- в модель книги картинки загружаются из панели администратора (log: mi pass:1) books-> выбрать книгу-> avatar-> кнопка выбрать файл-> сохранить
- список книг http://localhost:8000/
- читатели с книгами http://127.0.0.1:8000/readers/
- издатльства redactions/



