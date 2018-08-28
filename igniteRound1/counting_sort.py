#!/home/ankit/tensorflow/tfp/python3.5

def counting_sort(array1, max_val):
    m = max_val + 1
    count = [0] * m                
    
    for a in array1:
    # count occurences
        count[a] += 1             
    i = 0
    for a in range(m):            
        for c in range(count[a]):  
            array1[i] = a
            i += 1
    return array1
print(counting_sort([1,4,1,2,6,8,4,3,5,23,1,6,7,8,9,4,3],23))
