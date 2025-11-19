###
## Test file for the package simple_package
## Execute as 'python test_sp.py'
###

from simple_package import operations

if __name__ == '__main__':
    ## Define two numbers
    a = 1;
    b = 2;
    
    ## Print their sum with a nice message.
    print(f"The sum of {a} and {b} is {a + b}")

    ## Now do the same for the function in sp
    print(f"The product of {a} and {b} is {operations.multiply(a,b)}")

    # Note from editor: I have corrected the import line to specify the file - Line 6
    # Note from editor: I have also corrected the function from line 17