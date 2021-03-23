"""EX03 - avoid_fifth function."""

__author__: str = "730236759"

i = 0

def main() -> None:
    """Entrypoint of the program."""
    sentence = input("Type a sentence: ")
    avoid_fifth(sentence)
    print(avoid_fifth(sentence))
    
     
def avoid_fifth(sentence: str) -> str:
    """This Function will return a sentence without all "e"/"E"'s.""" 
    sentence_list = list(sentence)
    i = 0 
    while i < len(sentence_list):
        if sentence_list[i] == str("e"):
            sentence_list.pop(int(i))
        if sentence_list[i] == str("E"):
            sentence_list.pop(int(i))
        i += 1
        else: 
            i += 1
    i = 0
    while i < len(sentence_list):
        if sentence_list[i] == str("E"):
            sentence_list.pop(int(i))
        else:
            i += 1
    sentence_revised = str("")
    x = 0
    while x < len(sentence_list):
        sentence_revised += str(sentence_list[x])
        x += 1
    return sentence_revised


if __name__ == "__main__":
    main()
