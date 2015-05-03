from flask_wtf import Form 
from wtforms.validators import DataRequired
from wtforms import IntegerField

class LottoSetup(Form):
	number_of_draws = IntegerField('How Many Draws:')


