a=input("Enter the string")
s=list(a)
import os
def cl():
	os.system('cls')
flag=False
cl()
count=0
k=[]
q=[]
while flag!=True and count<len(s)*3:
	print("Guess a",len(s),"letter word")
	string=input()
	if string=='igiveup':
		print("The word was:",a)
		break
	if len(s)!=len(string):
		print("Please enter valid word")
	else:
		l=list(string)
		count+=1
		bull=0
		right=0
		if l==s:
			print("Hogaya Bhai!")
			print("Chances taken=",count)
			flag=True
		else:
			q=[]
			for i in range(len(l)):
				if l[i]==s[i]:
					bull+=1
					q.append(i)
			w=[i for i in s]
			
			for i in q:
				w[i]='#'
				l[i]='*'
			
			
			for i in range(len(l)):
				if l[i] in w: 
					right+=1
					w.remove(l[i])	
			print("Rights=",right,end=' ')
			print("Bulls=",bull)
			cl()
			print("All words guessed are:")
			k.append(string+' rights = '+str(right)+' Bulls = '+str(bull))
			for i in k:
				print(i)
			
if(flag!=True and count>=len(s)*3):
	print("Failed!")




