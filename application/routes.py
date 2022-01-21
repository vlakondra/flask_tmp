from application import app

# app = create_app()


@app.route("/")
@app.route("/index")
def index():
    return "hello привет!!!!"


@app.route("/test")
def tst():
    return "!!! hello привет!!!!"
