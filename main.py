from fractions import gcd


def read_file(filename: str) -> str:
	with open(filename) as file:
		for line in file:
			return line


def write_file(filename: str, elements: str) -> None:
	file = open(filename, 'w')
	for el in elements:
		file.write(el + ' ')
	file.close()


def main() -> None:
	list_ = []
	line = read_file('input.txt')
	split_line = line.split()
	for i in split_line:
		for j in split_line:
			if gcd(int(i), int(j)) == 1:
				need_append = '{} {}'.format(i, j)
				list_.append(need_append)
	write_file('output.txt', list_)


if __name__ == '__main__':
	main()