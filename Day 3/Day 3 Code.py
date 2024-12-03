import re
source = 'Day 3\Day 3 Prod.txt'

def importfile (source):                                                        ## Import file
    with open(source, "r") as f:   
        lines = "".join(f.readlines())
    return(lines)

def only_activated (input):                                                     ## First split on all don't()'s, "put first string in activated list". Split strings on all "Do()'s" discard index 0 and put the rest in the activated list.
    activated_list = []                             #Create empty list
    nodontlist = input.split("don't()")             #Split on all don't()'s
    activated_list.append(nodontlist[0])            #Put first string in activated list
    nodontlist.pop(0)                               #Remove first activated list

    for list in nodontlist:                         #Split on all do()'s
        component_list = list.split("do()")     
        component_list.pop(0)                       #Remove first deactivated list
        activated_list.append("".join(component_list))       
    output = "".join(activated_list)

    return(output)

def findmulvalue (input):                                                       ##Find all mul(number,number) and put them in a list
    result = []
    x = re.findall(r"mul\(\d+,\d+\)", input)
    result.append([list(map(int, re.findall(r'\d+', s))) for s in x])
    return(result)

def calculate_anw (input):                                                      ##Multiply all values for result
    awnser = int(0)
    for data in input:
        for result in data:
            datasum = result[0] * result[1]
            awnser = awnser + datasum
    print(awnser)

    awnser = 0

    
##Anwser 1
imported_data = importfile(source)
mul_values1 = findmulvalue(imported_data)
calculate_anw(mul_values1)


##Anwser 2
clean_mul_values = only_activated(imported_data)
mul_values2 = findmulvalue(clean_mul_values)
calculate_anw(mul_values2)



