#import library
import random
print("A number between 1 and 100")
num = random.randint(1,100)	#select a number
for guesses in range(1,6):
	print("Enter value")
	guessNum = int(input()) #user input for an integer
	#conditions
	if guessNum == num:
		print("Correct answer!! You guessed the number in " + str(guesses) + " times.")
		break
	else:
		if guessNum > num:
			print("The number is too high.")
		else:
			print("The number is too low.")
#telling the answer
if guessNum != num:
	print("I was thinking number " + str(num))