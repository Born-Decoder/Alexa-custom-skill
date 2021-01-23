import re

f = open(r"D:\Assignment and other works\Docs\physics.txt", "r+")
d = open(r"D:\Assignment and other works\Docs\some.txt", "r+")
reads = f.read()
result=[]
fish = []
lists = reads.split(". ")
lists = [k.lower() for k in lists]
for items in lists:
 result.append(re.sub("www.[a-z]*[\.][a-z]*"," ",items))
for j in result:
 fish.append(re.sub("\| .*[0-9]*"," ", j))

for i in fish:
 i = i.replace("\n", " ")
 d.write(i)

d.close()
f.close()

