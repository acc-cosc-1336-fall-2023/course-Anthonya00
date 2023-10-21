#

def get_p_distance(list1,list2):
    counter = 0 
    sum = 0
    if len(list1) != len(list2):
        raise ValueError ("Invalid")
    else:
        while counter < len(list1):
            if list1[counter] != list2[counter]:
                sum += 1
                counter += 1 
            else:
                counter += 1
    return round(sum/len(list1),5)

def get_p_distance_matrix(list1):
    n = len(list1)
    matrix = []
    for i in range(n):
        list = []
        for j in range(n):
            row = get_p_distance(list1[i],list1[j])
            list.append(row)
        matrix.append(list)
    return matrix












