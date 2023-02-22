#1/usr/bin/env python 3
"""

program_name.py
This is a template for the Advanced Topics class.
"""

__author__ = "Aria Wang"
__version__ = "the date" 

from atds import Deque

class PalindromeChecker(object):
    
    def __init__(self):
        self.strict = True

    def setStrictMode(self, strict):
        self.strict = strict
        return self.strict

    def isPalindrome(self, phrase):
        d = Deque()
        if self.strict == True:
            for char in phrase:
                d.add_rear(char)
            if d.is_empty():
                return False
            else:
                while d.is_empty() == False:
                    if d.size() == 1:
                        return True
                    elif d.remove_front() != d.remove_rear():
                        return False
                return True
        else:
            phrase = self.sanitize(phrase)
            for char in phrase:
                d.add_rear(char)
            if d.is_empty():
                return False
            else:
                while d.is_empty() == False:
                    if d.size() == 1:
                        return True
                    elif d.remove_front() != d.remove_rear():
                        return False
                return True

    def sanitize(self, phrase):
        phrase = phrase.lower()
        for char in phrase:
            if char not in "abcdefghijklmnopqrstuvwxyz":
                phrase = phrase.replace(char, "")
        return phrase


def main():
    p = PalindromeChecker()
    print("Palindrome Checker!")
    ans = input("Strict mode on (1) or off (2)?")
    if ans == "1":
        p.setStrictMode(True)
    else:
        p.setStrictMode(False)
    phrase = input("Phrase: ")
    if p.isPalindrome(phrase):
        print("Is a palindrome!")
    else:
        print("Not a palindrome")


if __name__ == "__main__":
    main()