import copy

crates = [[]]
num_list = []

with open('input.txt' , 'r') as f:

    guardian = False
    getLen = False      

    for r in f:
        i = 1
        counter = 0
        if(getLen == False):  ##Getting length of what our list will be
            for i in range(len(r)//4):
                row = []
                crates.append(row)
            getLen = True
            crates.pop() ##Removing the empty list
            
        
        if (guardian): #checking if we have passed the crates we are appending 

            nums = [int(num) for num in r.split() if num.isdigit()] ##getting digits of the lines and storing in a list
            if len(nums) == 3:
                num_list.append(nums)

        try:
            inputLen = int(len(r) // 4)
            m1 = r.strip().replace(" ", "").replace("\n", "")##remove whitespace and \n
            guardian = int(m1)
            guardian = True
            
        except ValueError:
            pass
        
        i = 1  #make sure the value of i 
        while(counter < len(r)//4 and not guardian):  #while we havent passed reading crates phase
                                                      #we read and append crates base on whitespaces
            if(r[i] != ' ' and i < len(r)):
                crates[counter].append(r[i])
            i += 4
            counter += 1 
            
            
# Loop over the rows in reverse order and swap them
for i in range(len(crates)):
    crates[i] = crates[i][::-1]
                       
def MoveCrates(cc,nn):     ##initiating operation
    for i in nn:
        i[1] -=1
        i[2] -=1
        reverse1 = cc[i[1]][-(i[0]):]
        reverse1 = reverse1[::-1] 
        cc[i[2]] += reverse1

        cc[i[1]] = cc[i[1]][:-(i[0])]
                  


print("###############################")
crates_clone = copy.deepcopy(crates)
num_list_clone = copy.deepcopy(num_list)

MoveCrates(crates_clone,num_list_clone)

output = []
for i in crates_clone:
    output.append(i[-1])
    print(i[-1])
    
print(output)

##End of part 1

def MoveCratesPart2(cc,nn):     ##initiating operation
    for i in nn:
        i[1] -=1
        i[2] -=1
        reverse1 = cc[i[1]][-(i[0]):]
        #reverse1 = reverse1[::-1] simply remove this line to be 2nd part RofL
        cc[i[2]] += reverse1

        cc[i[1]] = cc[i[1]][:-(i[0])]
                  

MoveCratesPart2(crates,num_list)

output2 = []
for i in crates:
    output2.append(i[-1])
    print(i[-1])
print(output2)