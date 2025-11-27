def compress(string: str):
	if len(string)==0:
		return string
	count=0
	current=string[0]
	encode=""
	for i in range(len(string)):
		if string[i].isnumeric():
			return "invalid input"
		elif i==len(string)-1 and string[i]==current:
			count+=1
			encode+=f"{current}{count}"
		elif i==len(string)-1 and not string[i]==current:
			encode+=f"{current}{count}"
			encode+=f"{string[i]}{1}"
		elif string[i]==current:
			count+=1
		else:
			encode+=f"{current}{count}"
			count=1
			current=string[i]
	return encode

def decompress(string: str):
	if len(string)!=0 and string[0].isnumeric():
		return "invalid input"
	output=""
	count=0
	while count<len(string):
		countCopy=count
		num=""
		for i in range(count+1, len(string)):
			if string[i].isnumeric():
				num+=string[i]
				count+=1
			else:
				break
		output+=f"{string[countCopy]*int(num)}"
		count+=1
	return output

def validString(lst: list):
	valid=[]
	for string in lst:
		if string.isalpha() or len(string)==0:
			valid.append(string)
	return valid

def anti67(lst: list):
	out=0
	remove=False
	for i in lst:
		if i==7 and remove:
			remove=False
		elif i==6 or remove:
			remove=True
		else:
			out+=i
	return out
