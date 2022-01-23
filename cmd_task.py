def task():
	from colorama import init
	init()
	from colorama import Fore, Back, Style
	from save_files import sve, open_files
	from time import sleep
	from random4 import randfloat
	stop=False
	files=open_files()
	for i in list(files.keys()):
		if i.split(".")[1]=="folder":
			file_pr=i
			break
	while stop!=True:
		li=False
		all__=input(file_pr+"/ ")
		task=all__.split(" ")[0]
		if task=="new":
			users=open('system/users.tsyst', 'a', encoding='UTF-8') # name===pasword"\n"name===pasword
			usr=input("Your name: ");pas=input("Your password: ")
			users.write(usr+"==="+pas+"\n")
			users.close()
			stop=True
		elif task=="stop":
			stop=True
		elif task=="del":
			if all__.split(" ")[1]=="all":
				file=open('system/users.tsyst', 'w', encoding='UTF-8')
				file.write("");file.close()
			stop=True
		# elif task=="cd":
		# 	if all__.split(" ")[1] in list(files[file_pr+".folder"]):

		# 	file_pr=file_pr+"/"+str(files[file_pr+".folder"].values())
		elif task=="dir":
			try:
				text=list(files[file_pr].keys())
			except: 
				b=file_pr.split("/")
				a=files[b[0]]
				del b[0]
				ln=len(b)
				for i in range(ln):
					try:
						r=a[b[0]]
					except:
						r=r[b[0]]
					del b[0]
				text=list(r.keys())
			abc=""
			for i in text:
				abc=abc+i+" "
			abc=abc.strip();abc=abc.replace(" ", " ; ")
			print(abc)
			print("\n")
		elif task=="cd":
			if all__.split(" ")[1]!="..":
				try:
					if all__.split(" ")[1].split(".")[1]=="folder":
						print("Open folder " + all__.split(" ")[1]+"\n")
						file_pr=file_pr+"/"+all__.split(" ")[1]
				except:
					for i in range(5):
						print("\033[31m--<System Error | Error #1>--")
						sleep(randfloat(0.003,1.500))
					print("\033[37m\n[R16]")
			else:
				try:
					file_pr22 = file_pr.split("/")
					del file_pr22[-1]
					aaa=""
					for i in file_pr22:
						aaa=aaa+"/"+i
					aaa=list(aaa)
					del aaa[0]
					aaa="".join(map(str, aaa))
					# aaa=list(aaa)
					# del aaa[-1]
					# aaa="".join(map(str, aaa))
					print("Open..."+"\n")
					file_pr=aaa
				except:
					for i in range(5):
						print("\033[31m--<System Error | Error #1>--")
						sleep(randfloat(0.003,1.500))
					print("\033[37m\n[R16]")

