import string
from map import locations
from player import characters
from items import items

#These 3 lists hold the key names that we do not want to skip.
key_characters = []
key_locations = []
key_items = []

for character in characters:
    key_characters.append(characters[character]['name'].lower())

for item in items:
    key_items.append(items[item]['name'].lower())

for location in locations:
    key_locations.append(locations[location]['name'].lower())
key_nouns = []
key_nouns.append(key_characters)
key_nouns.append(key_items)
key_nouns.append(key_locations)

key_verbs = [["go","move","walk", "run","wander","stroll"],
            ["take","seize","obtain","get","grab","grasp","collect","capture"],
            ["drop","abandon","dump","release"],
            ["give","transfer","hand","gift","deliver"],
            ["ride"],
            ["buy","purchase"],
            ["fight","attack","challenge","struggle","wrestle","tussle","hit"],
            ["talk","chat","speak","converse","tell","say"],
            ["help"]]

#add feature so both ID and name could be used in key_items
#def filter_nouns(word, key_nouns, filtered_words):
    #for nouns_list in key_nouns:
        #if word in nouns_list:
            #filtered_words.append(word)
    #return filtered_words

def filter_nouns(words, key_nouns, filtered_words):
    while words:
        for nouns_list in key_nouns:
            word = " ".join(words[:2])
            if word in nouns_list:
                filtered_words.append(word)
            elif words[0] in nouns_list:
                filtered_words.append(words[0])
            else:
                pass
        words=words[1:]
    return filtered_words

def filter_verbs(word, key_verbs, filtered_words):
    """
    """
    for verbs_list in key_verbs:
        if word in verbs_list:
            filtered_words.append(verbs_list[0])
        else:
            pass
    return filtered_words

def filter_words(words, key_verbs, key_nouns):
    filtered_words = []
    for word in words:
        filtered_words = filter_verbs(word, key_verbs, filtered_words)
    filtered_words = filter_nouns(words, key_nouns, filtered_words)

    return filtered_words

def remove_punct(text):
    """This function is used to remove all punctuation
    marks from a string. Spaces do not count as punctuation and should
    not be removed. The funcion takes a string and returns a new string
    which does not contain any puctuation. For example:

    >>> remove_punct("Hello, World!")
    'Hello World'
    >>> remove_punct("-- ...Hey! -- Yes?!...")
    ' Hey  Yes'
    >>> remove_punct(",go!So.?uTh")
    'goSouTh'
    """
    no_punct = ""
    for char in text:
        if not (char in string.punctuation):
            no_punct = no_punct + char

    return no_punct


def normalise_input(user_input, key_verbs, key_nouns):
    """This function removes all punctuation from the string and converts it to
    lower case. It then splits the string into a list of words (also removing
    any extra spaces between words) and further removes all "unimportant"
    words from the list of words using the filter_words() function. The
    resulting list of "important" words is returned.
    """
    # Remove punctuation and convert to lower case
    no_punct = remove_punct(user_input).lower()

    list_of_words = []
    word = ""
    for letter in no_punct:
        if letter.isspace() and word:
            list_of_words.append(word)
            word = ""
        elif not letter.isspace():
            word += letter
    if word:
        list_of_words.append(word)
    list_of_words = filter_words(list_of_words, key_nouns, key_verbs)

    return list_of_words
