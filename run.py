from flask import Flask, render_template, request, redirect, url_for
from powerball import number_generator
from forms import LottoSetup

app = Flask(__name__)
app.config.from_object('config.DevConfig')

@app.route('/home', methods=['GET', 'POST'])
def home():
    form = LottoSetup()
    if request.method == 'POST':
        return redirect(url_for('draw'))

    return render_template('draw_setup.html', form=form)

@app.route('/draw')
def draw():
    number, power = number_generator()
    return render_template('draw.html', number=number, power=power)    

if __name__ == '__main__':
    app.run()