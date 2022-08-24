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
    with open(directory, "w", encoding="UTF8") as f:
        f.write("")


def writer(string, directory="output.txt"):
    with open(directory, "a", encoding="UTF8") as f:
        f.write(string + "\n")


def random_suffix_from_list(suffixes):
    return random.choice(suffixes)


def random_prefix_from_list(prefixes):
    return random.choice(prefixes)


def random_common_word():
    return random.choice(user_input_list)


# ask user for input


def user_input():
    user_input_list_new = (input("Enter a common Word: "))
    user_input_list.append(user_input_list_new)
    # ask user for input, until user enters an empty string
    while user_input_list_new != "":
        user_input_list_new = (
            input("Enter a common word, if finished, press RETURN: "))
        user_input_list.append(user_input_list_new)
    return user_input_list


def generate(length: int):
    for _ in range(0, length):
        writer(random_prefix_from_list(prefixes) +
               str(random_common_word()) + random_suffix_from_list(suffixes),args.path)
    return True


def main(length: int):

    clear_text_file(args.path)

    animation = "|/-\\"

    generate(length)

    print("Done generating " + str(length) + " lines")


def interactive_mode():
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
