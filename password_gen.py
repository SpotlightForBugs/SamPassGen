# this script generates a String with 3 parts:
# 1. a prefix which is a random word from the dictionary
# 2. a common word which is a random word from the dictionary
# 3 a suffix which is a random word from the dictionary
# Multiple of these String are generated and saved in a file called output.txt


import random
import string
import time
import argparse


prefixes = [""]
for line in open("pre.txt"):
    prefixes.append(line.strip())


user_input_list = []
suffixes = [""]
for line in open("suff.txt"):
    suffixes.append(line.strip())


def clear_text_file(directory="output.txt"):
    """
    The clear_text_file function clears the contents of a text file.
    
    Parameters: 
    directory (str): The name of the directory to be cleared. Defaults to &quot;output.txt&quot;. 
    
    
    :param directory=&quot;output.txt&quot;: Specify the name of the file that will be created
    :return: The string &quot;&quot;
   
    """
    with open(directory, "w", encoding="UTF8") as f:
        f.write("")


def writer(string, directory="output.txt"):
    """
    The writer function writes a string to the specified file.
    The default directory is output.txt.
    
    :param string: Write the string to the file
    :param directory=&quot;output.txt&quot;: Specify the directory of the file that is being written to
    :return: None
   
    """
    with open(directory, "a", encoding="UTF8") as f:
        f.write(string + "\n")


def random_suffix_from_list(suffixes):
    """
    The random_suffix_from_list function takes a list of strings as input and returns one of the strings at random.
    
    
    :param suffixes: Pass a list of suffixes to the function
    :return: A random suffix from a list of suffixes
   
    """
    return random.choice(suffixes)


def random_prefix_from_list(prefixes):
    """
    The random_prefix_from_list function takes a list of prefixes as an argument and returns a random prefix from the list.
    
    
    :param prefixes: Pass a list of prefixes to the function
    :return: A random prefix from the list of prefixes
   
    """
    return random.choice(prefixes)


def random_common_word():
    """
    The random_common_word function returns a random word from the user input list.
    
    
    :return: A random word from the user input list
   
    """
    return random.choice(user_input_list)


# ask user for input


def user_input():
    """
    The user_input function asks the user to input a list of words, and stores them in a list.
    The function will continue to ask the user for input until they press RETURN without entering any text.
    This is useful when you want to prompt the user for multiple pieces of information.
    
    :return: A list of the user's input
   
    """
    user_input_list_new = (input("Enter a common Word: "))
    user_input_list.append(user_input_list_new)
    # ask user for input, until user enters an empty string
    while user_input_list_new != "":
        user_input_list_new = (
            input("Enter a common word, if finished, press RETURN: "))
        user_input_list.append(user_input_list_new)
    return user_input_list


def generate(length: int):
    """
    The generate function generates a random number of words, between 1 and the length specified by the user. 
    It then generates a random prefix from the list of prefixes, concatenates it with a common word from 
    the list of common words, and finally appends one of three suffixes to that string.
    
    :param length:int: Specify the number of random words to generate
    :return: True
   
    """
    for _ in range(0, length):
        writer(random_prefix_from_list(prefixes) +
               str(random_common_word()) + random_suffix_from_list(suffixes),args.path)
    return True


def main(length: int):
    """
    The main function of this script is to generate a file of random strings.


    :param length:int: Specify the number of lines to be generated
    :return: The string &quot;done generating &lt;length&gt; lines&quot;
   
    """

    clear_text_file(args.path)

    animation = "|/-\\"

    generate(length)

    print("Done generating " + str(length) + " lines")


def interactive_mode():
    """
    The interactive_mode function is a function that allows the user to input their own text and have it be converted into a Markov Chain. 
    The user will first be asked for how many lines they would like to generate, then they will be prompted for what type of text file they want to use. 
    If the user inputs &quot;none&quot;, then the program will default back to using an English corpus from NLTK's library.
    
    :return: The user_input function and the length variable
   
    """
    user_input()
    length = int(input("How many lines do you want to generate? "))
    main(length)


# generate argparse for all functions
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Generate a random password")
    parser.add_argument("-l", "--length", type=int, help="lines to generate")
    parser.add_argument("-i", "--interactive", action="store_true",
                        help="Interactive mode", default=True,dest="interactive")
    parser.add_argument("-c", "--common_words", type=str,
                        help="common words, delimited by :", action="store")
    parser.add_argument("-p", "--path", type=str,help="path to output file, defaults to output.txt", action="store",dest="path",default="output.txt")
    args = parser.parse_args()

    if (not args.interactive and not args.length and not args.common_words):
        print("Please specify -i for interactive mode or -l for length and -c for common words")
        exit(0)

    elif args.interactive and not args.length and not args.common_words:

        # interactive mode
        print("Missing arguments, entering Interactive mode", flush=True)

        interactive_mode()
    else:
        # split args.common_words delimited by :. Add each word to user_input_list_split
        user_input_list_split = args.common_words.split(":")
        # add each word to user_input_list
        for word in user_input_list_split:
            user_input_list.append(word)
        main(int(args.length))
