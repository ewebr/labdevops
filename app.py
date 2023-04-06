from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "This is the message of the challenge!"

if __name__ == '__main__':
    app.run()