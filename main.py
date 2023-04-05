crates = [[]]
num_list = []

with open('input.txt' , 'r') as f:

    guardian = False
    getLen = False

    for r in f:
        i = 1
        counter = 0
        if(getLen == False):
            for i in range(len(r)//4):
                row = []
                crates.append(row)
            getLen = True
            crates.pop()
            
        
        if (guardian):

            nums = [int(num) for num in r.split() if num.isdigit()]
            if len(nums) == 3:
                num_list.append(nums)

        try:
            inputLen = int(len(r) // 4)
            m1 = r.strip().replace(" ", "").replace("\n", "")
            guardian = int(m1)
            guardian = True
            
        except ValueError:
            pass
        i = 1
        while(counter < len(r)//4 and not guardian):
            
            if(r[i] != ' ' and i < len(r)):
                crates[counter].append(r[i])
            i += 4
            counter += 1 
            
            
# Loop over the rows in reverse order and swap them
for i in range(len(crates)):
    crates[i] = crates[i][::-1]
                       
def MoveCrates(crates,numbers):
    for i in numbers:
        i[1] -=1
        i[2] -=1
        reverse1 = crates[i[1]][-(i[0]):]
        reverse1 = reverse1[::-1] 
        crates[i[2]] += reverse1

        crates[i[1]] = crates[i[1]][:-(i[0])]
        
        
  
    
    
            
print(num_list)
print (crates)

print("###############################")
MoveCrates(crates,num_list)
output = []
for i in crates:
    output.append(i[-1])
    print(i[-1])
    
print(output)