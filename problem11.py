### Project Euler Problem 8
### Will Olson
### 27 February 2014
### Python 2.7.6

def filter_matrix( file_name ):
    fout = open(file_name, 'r')
    file_list = []

    ### Store the matix from the text file in a 2-dimentional array
    while (fout.readline() != ''):
        file_line = fout.readline()
        file_list.append(file_line.split())
    
    a, b, c = 0, 0, 0
    ### Iterate through row groups and test
    ### Iterate through column groups and check
    ### Iterate through slant right groups and check
    ### Iterate through slant left groups and check
    print file_list[:]
    fout.close()
    return a*b*c

user_file = raw_input("Enter the file name of the matix: ")
print filter_matrix(user_file)

### In progress
