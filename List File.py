#Jovanni Rubio Contreras
#Tuesday Nov. 16

y = 6
x = [1,2]

#create list

print("--->Everithing in my posetion")

inventory = ["bike","warm-up pants","car","lunch"]

#print variables

print(y)
print(x)

print(inventory)
print(inventory[2])

#first loop

print("--->Regular loop")


count = 1

while count < 4:
  print(inventory[count])
  count = count + 1
  
#second loop
  
print("--->Backward loop")
  
count = 3

while count > 0:
  print(inventory[count])
  count = count - 1
  
#for loop

print("--->The inventory for loop")
  
for count in inventory:
  print(count)
