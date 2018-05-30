import random
import sys

secret_number = random.randint(1, 100)
#secret_number = 50


#wish statement
print "Use your 3 wishes to guess the magic number!"
print "If you fail you will be fed to the Kraken!"


#wish checker function
def process_user_guess(asked_count):
    print "With your {} wish, which number would you like to wish upon?".format(asked_count)
    value = sys.stdin.readline()
    value = value.strip()
    int_value = int(value)

    if int_value == secret_number:
        print "You good sir have chosen wisely. You shall be spared, go on your way"
        return True

    elif int_value > secret_number:
        print "You have too high of a wish in mind,try again but think smaller!"
    else:
        int_value < secret_number
        print "You need a grander mind! Wish bigger!"
        return False


#checking for wished number if not guessed and proceeds to next one
guessed = process_user_guess("First")
if not guessed:
    guessed = process_user_guess("Second")
if not guessed:
    guessed = process_user_guess("Third")



#Wish number print
print "The magical number was:{}".format(secret_number)