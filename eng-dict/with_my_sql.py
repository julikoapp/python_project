import mysql.connector
import difflib
from difflib import SequenceMatcher, get_close_matches
connection = mysql.connector.connect(
    user="ardit700_student",
    password="ardit700_student",
    host="108.167.140.122",
    database="ardit700_pm1database"
)

cursor = connection.cursor()
def find_word(word):
    query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '{}'".format(word.lower()))
    results = cursor.fetchall()
    if len(results) == 0:
        print("Wait...")

        all_words = cursor.execute("SELECT * FROM Dictionary") #Here we get everything that Dictionary has
        results_all_words = cursor.fetchall() #here we get list with sets - results_all_words
        all_words_cl = [] # here is array for only words without meaning
        for result in results_all_words: # iterating through sets
            all_words_cl.append(result[0]) #getting first element in set - word

        possible_words = get_close_matches(word, all_words_cl) #finding close matches
        if len(possible_words) > 0:
            answer = input("Did you mean %s instead? If yes, type YES, else NO: " % possible_words[0])
            if answer == "YES":
                return find_word(possible_words[0])
        return "Oops, I don't know this word!"
    else:
        for result in results:
            return result[1]

word_from_user = input("Type here the word you are looking for: ")
print(find_word(word_from_user))
