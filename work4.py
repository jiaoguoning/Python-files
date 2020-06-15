import time 

def timer():
    def wrapper(func):
	time_1 = time.time()
	func()
	time_2 = time.time()
	return time_2 - time_1
    return wrapper 

@timer
def test():
    print(3 ** 3 - 78)

test() 
