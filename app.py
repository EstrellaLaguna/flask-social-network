from flask import Flask 
import configparser

app = Flask(__name__)
config = configparser.ConfigParser()
config.read('.env')


app.debug = config['DEFAULT']['DEBUG']
app.secret_key = config['DEFAULT']['SECRET_KEY']

@app.route("/")
def hello():
	return "Hello word"

if __name__ == "__main__":
	app.run()
