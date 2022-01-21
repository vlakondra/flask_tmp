Заметки.
Основной файл нужно называть или app.py или создавать переменную:типа set FLASK_APP=flask_tmp.py.
Сейчас используется файл .flaskenv

Задача: опубликовать этот простейший проект на yamaz.ru
-------------
обновил uwsgi c 2.0.15 до 2.0.20. Для root версия осталось прежней
и обнаружилось что для нее не установлены плагины, поэтому quickStart
не работает. Если работать как vkondra,  версия будет 2.0.20, плагины
имеются, quickStart работает. 
https://stackoverflow.com/questions/31330905/uwsgi-options-wsgi-file-and-module-not-recognized
----------------
Имеет смысл когда все наладится установить uwsgitop 
----------------

Fetch OR Clone??
Пока воспользовался этим:

git init    
git remote add origin [my-repo]
git fetch
git checkout origin/master -ft
и для отслеживания изменений
git pull origin master
Вроде на этом можно продолжить эксперименты с uwsgi
но все не просто
git mergetool  (!!!)


https://stackoverflow.com/questions/5377960/git-whats-the-best-practice-to-git-clone-into-an-existing-folder
---------------------
рабочий ini для простого py
[uwsgi]
socket = 127.0.0.1:3031
chdir = /home/vkondra/mydevs/test_uwsgi
wsgi-file = foobar.py
processes = 4
threads = 2
stats = 127.0.0.1:9191

nginx
-------
location / {
    include uwsgi_params;
    uwsgi_pass 127.0.0.1:3031;
}

рабочий ini для простого flask app
[uwsgi]
socket = 127.0.0.1:3031
chdir = /home/vkondra/mydevs/first-venv-test
virtualenv = /home/vkondra/.virtualenvs/first-venv-test
wsgi-file = myflaskapp.py
callable = app
processes = 4
threads = 2
stats = 127.0.0.1:9191
-------------------
app
-----------------
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<span style='color:red'>I am app 1</span>"