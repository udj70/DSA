def solve(plate_number,source,destination,helper):
    #base condition
    #when only one plate is left then simply transfer it from source to destination without helper stack
    if plate_number==1:
        print("move plate {0} from {1} to {2}".format(plate_number,source,destination))
        return
    #hypothesis 
    #below function will shift top n-1 plates from source to helper stack    
    solve(plate_number-1,source,helper,destination)
    #then simply shift last plate from source to destination stack
    print("move plate {0} from {1} to {2}".format(plate_number,source,destination))

    #again solve for n-1 plates present in helper to shift them to destionation with the help of source stack   
    solve(plate_number-1,helper,destination,source)
    return

s=1 #source stack representaion
h=2 #helper stack  representaion
d=3 #destination stack  representaion
solve(3,s,d,h) #solve for three plates in source stack

'''
    p1          _         _                      
    p2          _         _
    p3          _         _

    source     helper   destination



'''


