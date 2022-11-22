import re
import sys


def main():
    # TODO while loop to make smooth transition
    take_input()


def take_input():
    # Takes in user input and prints it out
    print("\nPassword Policy:"
          "\n\tAll passwords should be between 16 & 64 characters long"
          "\n\tAll passwords must not contain more than 4 digits in a row"
          "\n\tAll passwords must contain at least one Special character, one Lower-case letter, "
          "one Upper case letter, and one Number"
          "\n\tAll passwords must also not contain any words in the dictionary"
          "\n\n FYI: All spaces in the password will be removed\n")
    password = input("Please enter the Password you wish to check: ")
    # remove spaces from the password
    password = password.replace(' ', '')
    # input keywords
    keyword_list = []
    print("\nKeywords may include a Website Name, birth year, or other personal data.")
    while True:
        x = input("Please enter additional keywords or press Enter to exit: ")
        if not x:
            print("All keywords entered")
            break
        else:
            keyword_list.append(x)
    # passes the input to the checking method(s)
    regex_check(password, keyword_list)


def regex_check(password, keyword_list):
    # Checks the input password against password complexity rules
    check_passed = False

    # length checker
    password_length_check = False
    password_length = len(password)
    if (password_length >= 16) & (password_length <= 64):
        password_length_check = True
        print("Password is between 16 and 64 characters long")
    else:
        print("\tPassword is not between 16 and 64 characters long\n"
              "\tThe check has failed.")

    # special character checker
    password_special_characters = False
    special_character_list = "`~!@#$%^&*()_-+={[}}|\\:;\"'<,>.?/"
    for char in special_character_list:
        check = (char in password)
        if check:
            password_special_characters = True
            print("The Password contains at least one special character")
            break
    if password_special_characters is False:
        print("\tThe Password does not contain a special character\n"
              "\tThe check has failed.")

    # Upper case, Lower case, & digit checker
    password_character_checker = False
    password_lower_case_checker = bool(re.search(r'[A-Z]', password))
    password_upper_case_checker = bool(re.search(r'[a-z]', password))
    password_digit_checker = bool(re.search(r'[0-9]', password))
    if password_digit_checker & password_upper_case_checker & password_lower_case_checker:
        password_character_checker = True
        print("The password contains at least one Upper case letter, Lower case letter, and one Number")
    else:
        print("\tThe password does not contain at least one Upper case letter, Lower case letter, and one Number\n"
              "\tThe check has failed.")

    # 5 digits in a row checker
    # we don't want there to be sequences of more than 4 digits in a row
    password_5_digits = True
    digits = r'\d\d\d\d\d'
    check = re.search(digits, password)
    if not check:
        password_5_digits = False
        print("The password does not contain more than 4 digits in a row")
    else:
        print("\tThe password contains more than 4 digits in a row\n"
              "\tThe check has failed.")

    # keyword checker
    # checks to see if keywords entered earlier are in password
    password_keywords = False
    for x in keyword_list:
        check = (x in password)
        if check:
            password_keywords = True
            print("\n\t\"" + x + "\" has been found in the password.\n"
                                 "\tThe check has failed")
            break
    if password_keywords:
        print("No user entered keywords were found in the password")

    # dictionary checker: checks against dictionary words
    # will only run if all previous checks pass, otherwise will skip to save resources
    password_dict_checker = False
    if password_length_check & password_special_characters & password_character_checker & (password_5_digits is False) \
            & (password_keywords is False):
        print("Dictionary Word Checker is running.\n"
              "Found words will be printed below.\n"
              "This may take some time...\n")
        dict_file = open('words.txt', 'r')
        password_dict_checker = True
        # password_dict_words = (re.findall(dict_file.readline(), password))
        for line in dict_file:
            if (line.strip()) in password:
                print('\t\"' + line.strip() + "\" is an illegal word.")
                password_dict_checker = False

        # password_dict_checker = not bool(password_dict_words)
        dict_file.close()
    else:
        print("\nDictionary check skipped to save resources\n")

    # check if check passed
    if password_length_check & password_special_characters & password_character_checker & password_dict_checker \
            & (password_5_digits is False) & (password_keywords is False):
        check_passed = True

    if check_passed:
        print("\nPassword Check Passed!\n"
              + password + " is a good password\n")
    else:
        print("\nPassword Check Failed\n")
    # Have to add exit method call here or smooth_exit will not execute if check passes
    # Wtf??? This is dumb
    smooth_exit()


def smooth_exit():
    # exits the user out of the program smoothly
    # code from https://stackoverflow.com/questions/21759946/how-to-exit-program-using-the-enter-key
    exit_test = input("Press Enter to exit or input anything else to check another password: ")
    if not exit_test:
        print("Exiting the Password Checker...")
        sys.exit()
    else:
        take_input()


# Code placed here is executed when run in cmd line
if __name__ == '__main__':
    main()
