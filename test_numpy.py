import numpy as np

def concatenate_part():

    a = np.array([[1,2,3],[7,8,9],[10,11,12]])
    b = np.array([[4,5,6]])
    
    c = np.concatenate((a, b), axis=0)
    d = np.concatenate((a, b.T), axis=1)
    e = b.T
    print(c)
    print("")
    print(d)
    print("")
    print(e)
    print("\n================================\n")
    
def tile_part():
	a = np.array([1,2,3])
	d1 = np.tile(a, (2))
	d2 = np.tile(a, (3,2))
	d3 = np.tile(a, (4,3,2))
	print("d1:\n",d1,"\n")
	print("d2:\n",d2,"\n")
	print("d3:\n",d3,"\n")
	b = np.array([[4,5,6],[7,8,9]])
	c1 = np.tile(b, 2)
	c2 = np.tile(b, (2,3))
	print("c1:\n",c1,"\n")
	print("c2:\n",c2,"\n")
	print("\n================================\n")

def reshape_part():
	a = np.arange(1, 13, 1)
	b = a.reshape((2,6))
	c = b.reshape((6,2))
	d = a.reshape((2,2,3))
	print("a:\n",a)
	print("b:\n",b)
	print("c:\n",c)
	print("d:\n",d)
	print("\n================================\n")

if __name__ == '__main__':
	print("======= concatenate part =======\n")
	concatenate_part()
	print("======= tile part ==============\n")
	tile_part()
	print("======= reshape part ===========\n")
	reshape_part()