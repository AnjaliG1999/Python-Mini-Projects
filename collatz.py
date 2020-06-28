#function collatz
def collatz(number):
	if number % 2 == 0:	#even number
		return number // 2
	else:	#odd number
		return 3 * number + 1

print("Enter a number:")
try:
	num = int(input())
	while  num > 1:
		num = collatz(num)	#function call
		print(num)
except:	#resolving ValueError
	print("Enter an integer!!")