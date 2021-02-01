"""
File: anagram.py
Name: Willie Li
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""
# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

# Global variable
dictionary_list = []


def main():
    print(f'Welcome to stanCode "Anagram Generator" (or {EXIT} to quit)')
    read_dictionary()
    while True:
        s = input("Find anagrams for: ")
        if s == EXIT:
            break
        find_anagrams(s)


def read_dictionary():
    with open(FILE, 'r') as f:
        for line in f:
            # eliminate the new line(/n)
            dictionary_list.append(line[0:len(line)-1])


def helper(s, possible_word, current_string):
    if len(current_string) == len(s) and current_string in dictionary_list and current_string not in possible_word:
        possible_word.append(current_string)
        print("Found: ", current_string)
        print("Searching...")

    else:
        for i in range(len(s)):
            character = s[i]
            # get the index of first repeat word
            repeat_w_index = current_string.find(character)
            if character not in current_string \
                    or i != s.find(character) and current_string[repeat_w_index+1:].find(character) == -1:
                # choose
                current_string += character
                if has_prefix(current_string):
                    # explore
                    helper(s, possible_word, current_string)
                # un-choose
                current_string = current_string[:len(current_string)-1]


def find_anagrams(s):
    """
    :param s: a word for searching
    :return: list of anagrams
    """
    current_string = ''
    possible_word = []
    print("Searching...")
    helper(s, possible_word, current_string)
    print(len(possible_word), "anagrams: ", possible_word)


def has_prefix(sub_s):
    """
    :param sub_s: a character of the input string
    :return: boolean
    """
    for word in dictionary_list:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
