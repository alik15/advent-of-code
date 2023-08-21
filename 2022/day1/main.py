
first= 0
second= 0
third = 0
smallest = 0
temp = 0
count = 0
elf_num=0



with open('input.txt',) as inp:
    lines = inp.readlines()
    
    
        

    for line in lines:
        if line != "\n":
            smallest += int(line.strip())
           
    
            
        
        if line == "\n":           
            
            if third< smallest:
                temp = third
                third = smallest 
                smallest = temp
                
                if second<third:
                    temp = second
                    second = third
                    third = temp
                    
                    if first < second:
                        temp = first
                        first  = second
                        second = temp
                
             
            
                
            smallest = 0
           


print(first, first+second+third)

