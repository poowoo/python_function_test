
	#def __init__(self):
	#	print("hello class")
	#def haha(self):
	#	print("haha")
	#print("hello world")	
#a = test()
class fa_test():
	def __init__(self,a):
		self.num = a
		print("fa love")
class test(fa_test):
	def __init__(self, i, j = 0):
		super(fa_test,self).__init__()
		#super().__init__()
		self.i = i
		self.x = "xxx"
		self.y = "yyy"
		self.z = "zzz"
		self.j = j
		print("no fa init")
	def __str__(self):
		return str(self.x)
	def hello(self):
		print("hello " + self.__str__())
d = test(22, j = 40)
#print(d, "__init__"))
print(d.i)
print(d.j)
#print(d.num)
#print(d, "x"))
#print(d, "y"))
#print(d, "z"))
#print(d, "__str__"))
#print(d, "hello"))
	

