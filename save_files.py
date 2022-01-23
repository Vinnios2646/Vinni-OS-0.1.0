def sve(list):
	from pickle import dump, HIGHEST_PROTOCOL
	with open('system/files.tsyst', 'wb') as f:
		dump(list, f, HIGHEST_PROTOCOL)
def open_files():
	from pickle import load as ld
	with open('system/files.tsyst', 'rb') as f:
		data = ld(f)
	return data