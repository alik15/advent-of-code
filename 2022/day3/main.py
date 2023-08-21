
sum = 0
badge_vals=[]


#Divides list into two and finds the common element in both lists
def priority_char(str1):
    length= len(str1)
    first_compartment= str1[:int((length/2))]
    second_compartment= str1[int((length/2)):]
    
    both_chars="null"
    
    for char1 in first_compartment:
        for char2 in second_compartment:
            if char1 == char2:
                both_chars=char1
                
    return both_chars



#converting character into its ascii value and applying offset
def priority_val(char1):
        
    if char1.isupper() == True:
        return (ord(char1)-38)
        
    else:
       return (ord(char1)-96)
   
   

with open("example_input.txt") as inp:
    lines = inp.readlines()

#For part 1
for line in lines:
    
    sum+=priority_val(priority_char(line.strip()))
   
    #badge_vals.append(priority_val(priority_char(line.strip())))
    
#For part 2
def common_items_group(list1):
     return (set(list1[0]) & set(list1[1]) & set(list1[2]))
         

fin_sum=0
count = 0
elf_group =[]
for line in lines:
    
    elf_group.append(line)
    count+=1
    if count == 2:
       fin_sum= priority_val(priority_char(common_items_group(elf_group)))
        
        
    

print(fin_sum)



#Answer for part 1
print(sum)
    
    


"""
sum = 0
#Removing common values from the list
badge_vals=[*set(badge_vals)]
print(badge_vals)
#Calculating the sum of all ints a list
for item in badge_vals:
    sum +=item
    print(sum)
    

#Answer for part two ---with badge groups
print(sum)
"""



    