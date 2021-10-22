def add(x,y):
	return x + y

def Subtract(x,y):
	return x - y

def Division(x,y):
	if(y!=0):
		return x/y
	else:
		print('Invalid input for denominator')		

def Multiply(x,y):
	return x*y

def Power(x,y):
	if(a==0 and b==0):
		print('Invalid inputs for a and b')
	elif(a==0 and b==-1):
		print('Invalid inputs')
	else:
		return a^b