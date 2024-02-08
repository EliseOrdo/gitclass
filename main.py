
class GemStone:
	name: str

	def __init__(self) -> None:
		self.name = 'random'

	def getName(self) -> str:
		return self.name


class TimeStone(GemStone):
	def __init__(self) -> None:
		super().__init__()
		self.name = 'TimeStone'

	def back(amount: int) -> None:
		print('Rewinding...')


if __name__ == '__main__':
	print('Hello World')
	# This is the first script of the project


