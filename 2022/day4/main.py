



def any_overlap(inp):
    list1=[]
    elf1=[]
    elf2=[]
    inp = inp[:-1]
    list1=inp.split(",")
    elf1=list1[0].split("-")
    elf2=list1[1].split("-")
    
    
    
    
    return 0

def check_absolute_overlap(inp):
    list1=[]
    elf1=[]
    elf2=[]
    inp = inp[:-1]
    list1=inp.split(",")
    elf1=list1[0].split("-")
    elf2=list1[1].split("-")
    
    
    #part1
    if((int(elf1[0])>=int(elf2[0])) and (int(elf1[1])<=int(elf2[1]))):
        print(elf1,elf2)
        return 1 
        
    elif((int(elf2[0])>=int(elf1[0])) and (int(elf2[1])<=int(elf1[1]))):
            print(elf1,elf2)
        
            return 1
    
        
    
    
    


count=0 
    
    
    

with open('input.txt',"r") as inp:
    lines = inp.readlines()
    
    
for line in lines:
   if ( check_absolute_overlap(line)==1):
       count+=1
       
       
print(count)
    