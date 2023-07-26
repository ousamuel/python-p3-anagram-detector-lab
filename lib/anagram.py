# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, list):
        anagrams =[]
        for string in list:
            if(sorted(string) == sorted(self.word)):
                anagrams.append(string)
        return anagrams
    pass