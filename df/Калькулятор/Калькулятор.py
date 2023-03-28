class Calculator:
	def __init__(self, number):
		self.number = number

	def plus(self, num1 : int, num2 : int, old):
		if old == False:
			return num1 + num2
		elif old == True and num2 == 0:
			return self.number + num1
		else:
			return self.number + num1 + num2 

	def minus(self, num1, num2, old):
		if old == False:
			print('ff')
			return num1 - num2
		elif old == True and num2 == 0:
			print('f')
			return self.number - num1
		elif old == True:
			print(f'fdfd')
			return int(self.number) - num1 - num2

	def total(self, number):
		self.number = number

	def __str__(self):
		return str(self.number)


def main(Calculator):
	call = Calculator
	print('Введите значения num1 & num2: ')
	num1 = int(input('Введите первое значения: '))
	num2 = int(input('Введите второе значения: '))

	znak = input('Введите какую операцию над ними вы хотите проделать: ')
	if znak == '+':
		while znak == '+' or znak == '-':
			total = call.plus(num1, num2, False)
			print('Ответ: ', total)
			call.total(total)
			znak = input('Хотите дальше приплюсовывать число или минусовать: ')
			if znak == '+':
				print('Ваш ответ сохранится и будет дальше приплюсовываться к будущим данным')
				num1 = int(input('Введите первое значения: '))
				num2 = int(input('Введите второе значения: '))
				call.plus(num1, num2, old = True)
				call.total(total)
				print(call)
			elif znak == '-':
				print('Ваш ответ сохранится и будет дальше приплюсовываться к будущим данным')
				num1 = int(input('Введите первое значения: '))
				num2 = int(input('Введите второе значения: '))
				call.minus(num1, num2, old = True)
				call.total(total)
				print(call)
call = Calculator(0)
main(call)
