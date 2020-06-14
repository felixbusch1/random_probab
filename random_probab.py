from random import randint
import argparse
import sys
import matplotlib.pyplot as plt
import numpy as np


#Argument parsing setup
##########################################################################################
parser = argparse.ArgumentParser()

parser.add_argument("-n", "--number_of_items", type=int, dest="number_of_items", default=128,
                    help="Specify how many pseudo-random binary strings you want to generate. (default=128)")

parser.add_argument("-l", "--length_of_item", type=int, dest="length_of_item", default=8,
                    help="Specify how long each binary string shall be. (default=8)")
##########################################################################################


#Function name: generate_binary_str
#
#Parameters: length := the length of the string to be generated. 
#
#Description: This function generates a pseudo random binary string.
#
#Return value: string containing only 0s and 1s
def generate_binary_str(length):
    s = ""
    for _ in range(length):
        s += str(randint(0,1))

    return s


#Function name: generate_binary_strings
#
#Parameters: number_of_strings_to_generate := already explaint.
#            binary_string_length          := length of each binary string to be generated.
#
#Description: This function generates a set of pseudo-random binary strings and returns it as a list.
#
#Return value: list of binary string. (string contains only 0s and 1s)
def generate_binary_strings(number_of_strings_to_generate, binary_string_length):
    
    binary_strings = []
    for _ in range(number_of_strings_to_generate):
        binary_strings.append(generate_binary_str(binary_string_length))
    
    return binary_strings


# Function name: analyse_binary_string_list
#
# Parameters: binary_string_list   :=  list of random generated binary strings 
#             binary_string_length :=  length of each binary string
#
#
# Description: This function takes two parameters. The first is a list of
#              pseudo-random generated binary strings. And the second is the
#              length of each binary string in bytes. 
#
#              The function checks in which of the strings there is no "one", one "one", 
#              two "ones" etc. The number of strings with the same number of "ones" 
#              is stored in a list.
#
#              Example: 
#              
#              binary_string_list
#              [0100], [1010], [1100], [0111] 
#               
#              binary_string_length = 4
#
#              Output: [0, 1, 2, 1]
#              (no binary string with no ones, one binary string with a one, two with two ones 
#               and only one with three ones)
#
# Return value: list of the results

def analyse_binary_string_list(binary_string_list, binary_string_length):

    result = []
    iteration_counter = 0

    for i in range(binary_string_length+1):
        result.append(0)

    for _ in range(binary_string_length+1):

        for binarystr in binary_string_list:
            
            number_of_ones = 0
            for i in range(binary_string_length):
                
                if binarystr[i] == "1":
                    number_of_ones += 1
                
            if number_of_ones == iteration_counter:
                result[iteration_counter] += 1

        iteration_counter += 1

    return result


def main():
    args = parser.parse_args()
    data = generate_binary_strings(args.number_of_items, args.length_of_item)
    
    xlist = []
    xvalues = np.arange(0, args.length_of_item+1, 1)
    for x in xvalues:
        xlist.append(x)
    
    ylist = analyse_binary_string_list(data, args.length_of_item)
    
    plt.xlabel('Possible 1s in binary string')
    plt.ylabel('Counted 1s in binary string')
    plt.title('Distribution of 1s in random data')
    
    plt.scatter(xlist, ylist)
    plt.show()

if __name__ == "__main__":
    main()
   