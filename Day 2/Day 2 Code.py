source = 'Day 2\Day 2 Test.txt'
left_list = []
right_list = []
distances_list = []
simularity_score_list = []


def importfile (source): ## Import file
    with open(source, "r") as f:   
        lines = f.readlines()
        my_list = [line.strip() for line in lines]
        print(my_list)

print(source)

importfile(source)