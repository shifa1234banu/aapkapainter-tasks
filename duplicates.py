list = [1,2,3,2]
    
list.sort() 
 
    
new_list = sorted(set(list)) 
dup_list =[] 
    
    
for i in range(len(new_list)): 
        if (list.count(new_list[i]) > 1 ): 
            dup_list.append(new_list[i]) 
            
print(dup_list)  