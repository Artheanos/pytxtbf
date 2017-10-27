import sys

sors = open("characters.txt").read()
sors = "0".join(sors.split("\n"))

x=6;y=5

temp = ""
ltr=[]
h=0

x1=(x+1);y1=(y+1)

inp = input("input ---> ").lower()
print("")

for i in inp:
	ltr.append( x1*y1*(ord(i)) )

for x in range (y):

	for i in ltr:

		for j in range(i+h,i+h+6):
			temp+=sors[j]
		temp+=" "
	
	temp+="\n"
	h+= x1

print(temp)



al="+++++[>+++++++>++++++>++<<<-]>>++";a=0;b=0;c=1
temp = "0".join(temp.split("\n"))

for i in temp:

	if i == " ":
		if b:
			al+=b*"."+">"
		a+=1
		b=0;c=0
	elif i == "#":
		if a:
			al+=a*"."+"<"
		if c:
			al+="<"
		b+=1
		a=0;c=0

	elif i == "0":
		if b:
			al+=b*"."+">>.<"
		if a:
			al+=a*"."+">.<"
		#al+=("0")
		a=0;b=0;c=1

print(al)


'''
beggining
+++++
[
>
+++++++
>++++++>++
<<<-
]>>
++
'''



