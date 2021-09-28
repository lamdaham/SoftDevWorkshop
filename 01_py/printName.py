import random
names1 = ["Ella", "Ivan", "Justin"]
names2 = ["John", "Bob", "Peter"]

if (random.randint(0,1) == 0):
	print(names1[random.randint(0, len(names1)-1)])
else: 
	print(names2[random.randint(0, len(names2)-1)])

