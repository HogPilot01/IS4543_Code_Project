import re
import sys


def main():
    # TODO while loop to make smooth transition
    take_input()


def take_input():
    # Takes in user input and prints it out
    password = input("Please enter the Password you wish to check: ")
    # passes the input to the checking method(s)
    regex_check(password)


def regex_check(password):
    # Checks the input password against password complexity rules
    check_passed = False

    # length checker
    password_length = False
    if (len(password) >= 16) & (len(password) <= 64):
        password_length = True

    # special character checker
    password_special_characters = False
    special_character_list = "`~!@#$%^&*()_-+={[}}|\\:;\"'<,>.?/"
    for char in special_character_list:
        check = (char in password)
        if check:
            password_special_characters = True
            break

    # Upper case, Lower case, & digit checker
    password_character_checker = False
    password_lower_case_checker = bool(re.search(r'[A-Z]', password))
    password_upper_case_checker = bool(re.search(r'[a-z]', password))
    password_digit_checker = bool(re.search(r'[0-9]', password))
    if password_digit_checker & password_upper_case_checker & password_lower_case_checker:
        password_character_checker = True

    # 5 digits in a row checker
    # we dont want there to be sequences of more than 4 digits in a row
    password_5_digits = True
    digits = r'\d\d\d\d\d'
    check = re.search(digits, password)
    if not check:
        password_5_digits = False

    # dictionary checker: checks against dictionary words
    # will only run if all previous checks pass, otherwise will skip to save resources
    #    password_dict_check_run = False
    #    if password_length & password_special_characters & password_character_checker & (password_5_digits is False):
    #        password_dict_check_run = True
    #        dict_file = open('words.txt', 'r')
    #        password_dict_checker = bool(re.findall(password, dict_file.read()))
    #    else:
    #        print("dictionary check skipped ")
    #        # TODO skip dict check

    # check if check passed
    if password_length & password_special_characters & password_character_checker & (password_5_digits is False):
        check_passed = True

    if check_passed:
        print("\nPassword Check Passed!\n")
    else:
        # TODO Print what went wrong
        print("\nPassword Check Failed\n")
    # Have to add exit method call here or smooth_exit will not execute if check passes
    # Wtf??? This is dumb
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
