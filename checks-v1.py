# 62 = 
print("==============================================================")
print("==============================================================")
print("")
print("H A S H   C H E C K E R     by thbgnnr")
print("")
print("==============================================================")
print("")

while True:
	h1 = (str(input("[>]   Hash nº 1: ")))
	h2 = (str(input("[>]   Hash nº 2: ")))
	if h1 == h2:
		print("")
		print("[!]   EXACT HASH!")
		print("")
	else:
		print("")
		print("[!]   DIFFERENT HASH")
		print("")
	yn = (str(input("[>]   Check another hash y/n? ")))
	if yn == "n":
		print("")
		print("[!]   Exiting...")
		print("")
		break
	else:
		print("")
		continue
