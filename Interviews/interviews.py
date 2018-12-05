def list_products(lst):
    left_lst = [1]
    right_lst = []
    left_num = 1
    right_num = 1
    for i in range(len(lst) - 1):
        left_num *= lst[i]
        right_num *= lst[len(lst) - (i+1)]
        left_lst.append(left_num)
        right_lst.insert(0,right_num)
    right_lst.append(1)
    
    new_lst = []
    for i in range(len(left_lst)):
        new_lst.append(left_lst[i] * right_lst[i])
    
    return new_lst

def overlap(r1,r2):
    r1['ux'] = r1.x + r1.w 
    r1['uy'] = r1.y + r1.h

    r2['ux'] = r2.x + r2.w 
    r2['uy'] = r2.y + r2.h

    if((r2.ux <= r1.ux and r2.uy <= r1.uy) and (r2.x >= r1.x and r2.y >= r1.y)):
            # rectangle is fully enclosed
            return r2
            
    if((r2.ux >= r1.ux and r2.uy >= r1.uy) and (r2.x <= r1.x and r2.y <= r1.y)):
            # rectangle is fully enclosed
            return r1

    if(r2.x <= r1.ux and r1.y <= r2.uy) and (r2.x >= r1.x and r2.y >= r1.y)):
        # rectangles overlap
        
        else:
            # only section rectangles overlap only

            
         


