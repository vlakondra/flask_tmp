from flask import Flask


def create_app():
    app = Flask(__name__)  # app - экз-р класса Flask, к-й становится членом пакета app
    print("__name__: ", __name__, app.instance_path, "<->", app.static_url_path)

    return app


app = create_app()

from application import routes  # app - ссылка на пакет app
