import json
import difflib
from difflib import SequenceMatcher, get_close_matches

eng_dict = json.load(open("data.json"))

def translate(word):
    """
    Function input is word that you're looking for in dictionary
    Output: meaning of the word
    """

    if word.lower() not in eng_dict:

        #1st
        #possible_word = []
        # for word_in_dict in eng_dict.keys():
        #     if SequenceMatcher(None, word_in_dict, word).ratio() * 100 > 80:
        #         possible_word.append(word_in_dict)

        #better practice
        possible_word = get_close_matches(word, eng_dict.keys())
        if len(possible_word) > 0:
            #
            #return "Maybe you have meant " + ",".join(i for i in possible_word)
            #return "Did you mean %s instead?" % get_close_matches(word, eng_dict.keys())[0]
            #answer = input("Did you mean %s instead? If yes, type YES, else NO: " % get_close_matches(word, eng_dict.keys())[0])

            answer = input("Did you mean %s instead? If yes, type YES, else NO: " % possible_word[0])
            if answer == "YES":
                #return eng_dict[get_close_matches(word, eng_dict.keys())[0]] #not formated!!
                return translate(get_close_matches(word, eng_dict.keys())[0])  #formated and логично
        return "Sorry, I can't find this word. \nPlease check up if you write it correct!"
    else:
        return "\n".join(i for i in eng_dict[word.lower()])


word_from_user = input("Enter the word here: ")
print(translate(word_from_user))