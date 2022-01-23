def cmd_start():
	from time import sleep
	from random4 import randfloat
	from os import mkdir
	from read_file import red
	from cmd_task import task
	from save_files import sve, open_files
	files={}
	try:
		open('system/users.tsyst', 'a', encoding='UTF-8')
	except:
		mkdir('system/')
	users=open('system/users.tsyst', 'a', encoding='UTF-8') # name===pasword"\n"name===pasword
	sr=red('system/users.tsyst')
	if sr==None:
		usr=input("Your name: ");pas=input("Your password: ")
		users.write(usr+"==="+pas+"\n")
	else:
		tr=False
		tb=False
		while tb!=True:
			usr=input("User: ")
			if usr in sr.keys():
				tb=True
			else:
				print("Error")
		while tr!=True:
			pas=input("Your password: ")
			if pas==sr[usr]:
				tr=True
			else:
				print("Error")
	try:
		files=open_files()
		files["C:.folder"]
	except:
		files__={
			"C:.folder":{
				"users.folder":{},
				"READ_ME.txt":"Hello!||This is \"VINNI OS\"!||XD"
			}
		}
		sve(files__)
		del files__
	files=open_files()
	print("\tLoading...")
	sleep(randfloat(0.200,2.200));print("\t\tHello "+usr+"!")
	task()
