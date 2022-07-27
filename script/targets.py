
# Woking on input taking process 
number = int(input("Enter number of Domains : "))
target_list = []


#Domains saving part
with open("/tmp/targets.txt", 'w') as target:
    for i in range(number):
        target_list.append(input('['+str(i+1)+'] Enter Target : ')+'\n')
        target.write(target_list[i])
target.close()
target_list = []
