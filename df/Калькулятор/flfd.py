class F:
	def __init__(self, num):
		self.num = num

	def total(self, num):
		self.num = num

	def __str__(self):
		return str(self.num)

f = F(0)
print(f)
f.total(43)
print(f)