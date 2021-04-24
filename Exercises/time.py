import time

def madlib():
    adjective=input("Enter an adjective: ")
    noun=input("Enter a Noun: ")
    pronoun=input("Enter a pronoun: ")

    fun_word=pronoun+ " is a "+ adjective +" "+ noun
    print(fun_word)

while True:
    madlib()
    time.sleep(5)