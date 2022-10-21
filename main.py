import re
import sys


def main():
    take_input()
    smooth_exit()


def take_input():
    # Takes in user input and prints it out
    password = input("Please enter the Password you wish to check: ")
    # passes the input to the checking method(s)
    regex_check(password)


def regex_check(password):
    # Checks the input password if it contains an illegal entry
    # in this case, the word password
    check = re.search("password", password)
    if check:
        print("Illegal word(s) found: " + check.group())
        # Have to add exit method call here or smooth_exit will not execute if check passes
        # Wtf??? This is dumb
        smooth_exit()
    else:
        print("Password Check Passed!")
        smooth_exit()


def smooth_exit():
    # exits the user out of the program smoothly
    # code from https://stackoverflow.com/questions/21759946/how-to-exit-program-using-the-enter-key
    exit_test = input("Press Enter to exit or input anything else to check another password: ")
    if not exit_test:
        print("Exiting the Password Checker")
        sys.exit()
    else:
        take_input()


# Code placed here is executed when run in cmd line
if __name__ == '__main__':
    main()
