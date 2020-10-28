#we only multiply when some logic is nested
# when code is stacked sequentially on top of one another we add their respective runtimes

def do_a_bunch_of_stuff(items):
    last_idx = len(items) - 1 # getting the length is O(1)
    print(items[last_idx])  # accessign an array element via index O(1). We'll consider printing O(1)
    
    middle_idx = len(items) / 2 # arithmetic operation and initializing a variable - O(1)
    idx = 0
    while idx < middle_idx: # this loop only runs over half out items
        print(items[idx])   # 1000 * n = O(1)
        idx = idx + 1
        
        
    for num in range(2000): #O(1) because 2000 doesn't change 
        print(num)          # O(1)