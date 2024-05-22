def right_angle_perimeter(number: int):
    lst=[]
    for i in range(1,number):
        for j in range(i,number):
            for k in range(j,number):
                if i**2+j**2==k**2 and i+j+k==number:
                    lst.append([i,j,k])
    return lst

max_lst=[]
for i in range(1,1001):
    if len(max_lst)<len(right_angle_perimeter(i)):
        max_lst=right_angle_perimeter(i)
        print(i,max_lst)