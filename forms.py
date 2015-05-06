from flask_wtf import Form 
#from wtforms.validators import DataRequired, NumberRange
from wtforms import IntegerField, validators, DecimalField

class LottoSetup(Form):
	number_of_draws = IntegerField('How Many Draws:',[validators.NumberRange(min=1, max=99)])
	cost_of_draw = DecimalField('Cost of a Draw: ', places =2, rounding=None)


