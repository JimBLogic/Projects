import argparse #import the argparse module
parser = argparse.ArgumentParser() #create an ArgumentParser object
parser.add_argument("-s", help="string to be reversed") #add a positional argument
args = parser.parse_args() #parse the arguments and store in a namespace

#make me a function that takes in a string and returns that string in reverse
def reverse_string(string):
    return string[::-1] #return the string in reverse

print(reverse_string(args.s)) #print the reversed string
