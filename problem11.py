### Project Euler Problem 8
### Will Olson
### 27 February 2014
### Python 2.7.6

def filter_matrix( file_name ):
    fout = open(file_name, 'r')
    fout.close()

user_file = raw_input("Enter the file name of the matix: ")
print filter_matrix(user_file)

### In progress
