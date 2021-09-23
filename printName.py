# Ivan Lam
# SoftDev
# K<nn> -- <Title/Topic/Summary... (Aim for concision, brevity, CLARITY. Write to your future self...)>
# 2021-09-21


import random
names1 = ["Ella", "Ivan", "Justin"]
names2 = ["John", "Bob", "Peter"]

if (random.randint(0,1) == 0):
	print(names1[random.randint(0, len(names1)-1)])
else: 
	print(names2[random.randint(0, len(names2)-1)])

