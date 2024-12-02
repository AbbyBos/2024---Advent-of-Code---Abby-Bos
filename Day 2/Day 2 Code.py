source = 'Day 2\Day 2 Prod.txt'
report_list = []
valid_count = 0


def importfile (source): ## Import file
    with open(source, "r") as f:   
        lines = f.readlines()
        my_list = [line.strip() for line in lines]
        for report in my_list:
            int_report = []
            for item in report.split():
                int_report.append(int(item))
            report_list.append(int_report)

def checksafe (report, valid_count): ## Main function generate a test report and check order and growth of values.
    for report in report_list:
        for i, level in enumerate(report):
            test_report = report.copy()
            del test_report[i]
            valid_order = ordercheck(test_report)
            valid_growth = checkgrowth(test_report)
            if valid_order == True and valid_growth <= 0:
                valid_count += 1
                break
    return(valid_count)


def checkgrowth (report): ## Check growth of values
    start = int(report[0])
    bad_growth_count = 0
    for i, level in enumerate(report):
        level = int(level)
        growth = abs(start - level)
        start = level
        if i != 0 and growth > 3 or i != 0 and growth == 0:
            bad_growth_count += 1
    return(bad_growth_count)


def ordercheck(report):  ## Check order of list for consistancy in ascending/dece
    if sorted(report) == report:
        valid_order = True
        return(valid_order)
    elif sorted(report, reverse=True) == report:
        valid_order = True
        return(valid_order)
    else:
        valid_order = False
        return(valid_order)
                    
importfile(source)
valid_count = checksafe(report_list, valid_count)
print(valid_count)
