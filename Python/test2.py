def uniqueZip(a: list, b:list):
	out=[]
	for i in a:
		for j in b:
			if (i,j) not in out:
				out.append((i,j))
	return out

def matchingChars(str: str):
	out=0
	for i in range(len(str)-1):
		if str[i]=="#" or str[i+1]=="#":
			continue
		elif str[i]=="*" or str[i+1]=="*":
			out+=1
		elif str[i]==str[i+1]:
			out+=1
	return out

def peaks(target: int):
	out=[]
	if target==0:
		return out
	if target<0: #thanks Eric, im dumb
		for i in range((target-1)*-1):
			out.append(-i)
		for i in range((target+1)*-1,0, -1):
			out.append(-i)
		out.append(0)
	else:
		for i in range(target+1):
			out.append(i)
		for i in range(target-1,0,-1):
			out.append(i)
		out.append(0)
	return out


def reverseAlpha(str: str):
	out=""
	for i in range(-1,-(len(str))-1,-1):
		if str[i].isalpha():
			out+=str[i]
	return out
