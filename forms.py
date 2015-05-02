from flask_wtf import Form 
from wtforms.validators import Required, NumberRange
from wtforms import IntegerField

class LottoSetup(Form):
	number_of_draws = IntegerField(
		'How Many Draws', validators=[Required(
			'You must enter a number of draws to continue'),NumberRange(min=1, max=100)])


