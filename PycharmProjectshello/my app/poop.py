def maximum_number(numbers):
    listing = numbers.split(", ")
    final_list = []
    highest_number = 0
    for values in listing:
        values = int(values)
        final_list.append(values)
    for each_number in final_list:
        if each_number > highest_number:
            highest_number = each_number
    return highest_number


good = open('name.txt', 'r')
print(good)
