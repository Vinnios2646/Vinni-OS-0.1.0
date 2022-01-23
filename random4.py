def randfloat(num_1,num_2):
	from random import randint
	num1=str(num_1).split(".");num2=str(num_2).split(".")
	rnd1=randint(int(num1[0]), int(num2[0]))
	rnd2=randint(int(num1[1]), int(num2[1]))
	num=eval(str(rnd1)+'.'+str(rnd2))
	return num