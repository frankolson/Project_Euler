### Project Euler Problem 8
### Will Olson
### 01 July 2013
### Python 2.7.5


def iterate_through_file( file_name ):
    fout = open(file_name, 'r')
    file_line = fout.readline()
    file_list = list(file_line)
    count = 0
    highest = 0
    while count < len(file_list)-5:
        product = int(file_list[count])*int(file_list[count+1])*int(file_list[count+2])*int(file_list[count+3])*int(file_list[count+4])
        if product > highest:
            highest = product
        count += 1
    fout.close()
    return highest

user_file = raw_input("enter a file name: ")
print iterate_through_file(user_file)
