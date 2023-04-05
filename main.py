crates = [[]]
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
            
        
        if (guardian):
            num_list = []

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
                       
        

print (crates)