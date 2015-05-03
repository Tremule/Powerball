from flask import Flask, render_template, request, redirect, url_for, flash
from powerball import number_generator
from forms import LottoSetup

app = Flask(__name__)
app.config.from_object('config.DevConfig')

@app.route('/', methods=['GET', 'POST'])
def home():
    form = LottoSetup()
    if request.method =='POST':
        if request.form['submit'] == 'draw' and form.validate_on_submit():
            number, power = number_generator()
            return render_template('draw.html',
                number=number, power=power, num_draw=form.number_of_draws.data)

        else:
            flash('Something went wrong, try again')
            return render_template('draw_setup.html', form=form)

    return render_template('draw_setup.html', form=form)


if __name__ == '__main__':
    app.run()