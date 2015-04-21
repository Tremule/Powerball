from flask import Flask, render_template
from powerball import number_generator

app = Flask(__name__)
app.config.from_object('config.DevConfig')

@app.route('/')
def hello_world():
	number, power = number_generator()
	return render_template('base.html', number=number, power=power)


if __name__ == '__main__':
    app.run()