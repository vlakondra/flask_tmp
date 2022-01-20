from flask import Flask

app = Flask(__name__)  # app - экз-р класса Flask, к-й становится членом пакета app
print("__name__: ", __name__)

from application import routes  # app - ссылка на пакет app
