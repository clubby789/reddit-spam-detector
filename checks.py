import listOfWords
from fuzzywuzzy import fuzz
from fuzzywuzzy import utils
from mocks import mockTitle, mockBody

def is_rule_breaking(ratio):
    return ratio > 50

def fuzzy_check(postTitle: str = "", postBody:str = ""):
    ratio = fuzz.partial_ratio([utils.full_process(postTitle), utils.full_process(postBody)], listOfWords.words['vote-manipulation'])
    print(ratio)
    if (not is_rule_breaking(ratio)):
        ratio = fuzz.partial_token_sort_ratio([postTitle, postBody], listOfWords.words['vote-manipulation'])
        print(ratio)

    return is_rule_breaking(ratio)

if __name__ == "__main__":
    print(fuzzy_check(mockTitle, mockBody))