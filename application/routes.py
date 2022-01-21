from application import app

# app = create_app()


@app.route("/")
@app.route("/index")
def index():
    return "<h1 style='width:400px; margin:0 auto'>hello привет!!!!</h1>"


@app.route("/test")
def tst():
    return "<h2 style='color:blue'>!!! hello привет!!!!</h2>"
