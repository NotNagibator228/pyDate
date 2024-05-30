from sys import argv, exit

argb = [ False for _ in range(0, 4) ]
argo = (
	'version',
	'about',
	'help'
)

suck = ( 0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5 )
dick = ( 4, 3, 1, 6 )
month = ( 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 )

moshonka = (
	"Понедельник",
	"Вторник",
	"Среда",
	"Четверг",
	"Пятница",
	"Суббота",
	"Воскресенье"
)
mount = (
	'Январь',
	'Февраль',
	'Март',
	'Апрель',
	'Май',
	'Июнь',
	'Июль',
	'Август',
	'Сентябрь',
	'Октябрь',
	'Ноябрь',
	'Декабрь'
)

def errorargs(errormessange : str, exitcode : int, echohelp : bool = True) -> None:
	print (f'Error {errormessange}')
	if echohelp: print (argo[2])
	exit (exitcode)

def isdick(age : int) -> bool:
	if age % 4 == 0:
		if age % 100 == 0 and age % 400 != 0:
			return False
		return True
	return False

def isopositdick(age : int, m : int, day : int) -> bool:
	if day < 1: return False
	if isdick(age) and m == 1 and day > 29: return False
	elif day > month[m]: return False
	return True

def getweek(age: int, m : int, day : int) -> int:
	age %= 400
	temp0, temp1 = divmod(age, 100)
	day += dick[temp0] + temp1 + suck[m]
	day += temp1 // 4
	
	if temp1 % 4 == 0 and temp1 > 3: day -= 1
	if temp0 == 0 and age > 0: day += 1
	if isdick(age) and m > 1: day += 1
	
	return day % 7

def main():
	if len(argv) == 1: errorargs("no argument's", 1)
	indices = []
	index : int = 1
	
	while index < len(argv):
		if argv[index][0] == '-':
			if argv[index][1] == '-':
				match argv[index][2:]:
					case 'version': argb[0] = True
					case 'about': argb[1] = True
					case 'help': argb[2] = True
					case _: errorargs(f'no agument: {argv[index][2:]}', 2)
			else:
				for char in argv[index][1:]:
					match char:
						case 'v': argb[0] = True
						case 'a': argb[1] = True
						case 'h': argb[2] = True
						case _: errorargs(f'no key: {char}', 3)
				
		elif (len(argv) - index) > 2:
			add : bool = True
			while index < len(argv):
				if add:
					if (len(argv) - index) > 2 and argv[index].isdigit():
						indices.append(index)
						index += 3
					else: break
				elif argv[index] == ',': index += 1
				else: break
				add = not add
			if len(indices) == 0: errorargs('not numbers', 5)
			continue
		else: errorargs('logick args', 4, False)
		index += 1

	for index in range(0, 3):
		if (argb[index]):
			print (argo[index])
			argb[3] = True
	if argb[3]: exit(0)

	for index in indices:
		age : int = int(argv[index])
		m : int = int(argv[index + 1]) - 1
		day : int = int(argv[index + 2])
		if not isopositdick(age, m, day): errorargs('dick date', 7, False)
		week : int = getweek(age, m, day)
		print (f'{age}, {m + 1} {mount[m]}, {day} = {week}, {moshonka[week]}')

if __name__ == '__main__': main()
