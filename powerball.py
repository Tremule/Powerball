from random import randint

def number_generator():
	draw = []
	while len(draw) < 5:
		ballvall = randint(1,53)
		if ballvall in draw:
			pass
		else : 
			draw.append(ballvall)
	powerball = (randint(1,42))
	return str(sorted(draw)).strip('[]'), powerball	

def draw_number(sets):
	for i in range(sets):
		draw = number_generator()
		return('Your numbers: {:<2}    \tPowerball: {}'.format(str(draw[0]).strip('[]'),draw[1]))


if __name__ == "__main__":
	print('Official (but fruitless) Powerball number generator') 
	try:
		number_of_draws = int(input('How many sets of numbers? >> '))
		draw_number(number_of_draws)
	except ValueError:
		print("That isn't a number, please try again")
