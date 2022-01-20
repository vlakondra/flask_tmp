from flask import Flask

app = Flask(__name__)  # app - экз-р класса Flask, к-й становится членом пакета app
print("__name__: ", __name__, app.instance_path, "<->", app.static_url_path)

from application import routes  # app - ссылка на пакет app
