source = 'Day 1\Day 1 Prod.txt'
left_list = []
right_list = []
distances_list = []
simularity_score_list = []

def importfile (source): ## Import file and output left and right list.
    with open(source, "r") as f:   
        lines = f.readlines()
        my_list = [line.strip() for line in lines]
        for line in my_list:
            datapoints = line.split()
            left_list.append(int(datapoints[0]))
            right_list.append(int(datapoints[1]))
    left_list.sort()
    right_list.sort()

def sortlist(list):  ##Sort a list
    list.sort()
    return list

def distances(list1, list2): #Calculate the distance between two lists.
    for i, data in enumerate(list1):
        distance = abs(data - list2[i])
        distances_list.append(distance)
    print('The awnser to part 1 is:',sum(distances_list))

def simularity(list1, list2): #Calculate the simularity between two lists.
    for i, data in enumerate(list1):
        list2.count(data)
        simularity_score = data * list2.count(data)
        simularity_score_list.append(simularity_score)
    print('The awnser to part 2 is:', sum(simularity_score_list))


importfile(source)
sortlist(left_list)
sortlist(right_list)
distances(left_list, right_list)
simularity(left_list, right_list)

