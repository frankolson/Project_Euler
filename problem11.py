### Project Euler Problem 8
### Will Olson
### 27 February 2014
### Python 2.7.6
### Last edit: 09 September 2014

def filter_matrix( file_name ):
    fout = open(file_name, 'rU')
    file_list = []

    # Answer variable
    maxP = 0

    ### Store the matix from the text file in a 2-dimentional array
    for line in fout:
        file_list.append(line.strip().split(' '))

    file_list = [[int(j) for j in i] for i in file_list]
    
    print file_list[:]
    fout.close()

    # Check horizontily
    for i in range(len(file_list)):
        for j in range(len(file_list[i])-3):
            h = (file_list[i][j])*(file_list[i][j+1])*(file_list[i][j+2])*\
                (file_list[i][j+3])

            if h > maxP:
                maxP = h
    
    # Check vertically
    for i in range(len(file_list[i])-3):
        for j in range(len(file_list)):
            v = (file_list[i][j])*(file_list[i+1][j])*(file_list[i+2][j])*\
                (file_list[i+3][j])

            if v > maxP:
                maxP = v

    # Check left diagonal
    for i in range(3, len(file_list[i])):
        for j in range(len(file_list)-3):
            leftD = (file_list[i][j])*(file_list[i-1][j+1])*(file_list[i-2][j+2])*\
                (file_list[i-3][j+3])

            if leftD > maxP:
                maxP = leftD

    # Check right diagonal
    for i in range(len(file_list[i])-3):
        for j in range(len(file_list)-3):
            rightD = (file_list[i][j])*(file_list[i+1][j+1])*(file_list[i+2][j+2])*\
                (file_list[i+3][j+3])

            if rightD > maxP:
                maxP = rightD
    
    return maxP

user_file = raw_input("Enter the file name of the matix: ")
print filter_matrix(user_file)
