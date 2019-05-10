import requests
from bs4 import BeautifulSoup
import operator
from operator import attrgetter

def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, "html.parser")
    for post_text in soup.findAll("a",{"class": "title text-semibold"}):
        content = post_text.string
        words = content.lower().split()
        for each_word in words:
            word_list.append(each_word)
    clean_up_list(word_list)

def clean_up_list(word_list):
    clean_word_list = []
    for word in word_list:
        symbols = r"!@#$%^&*()_+\"<>?,./;'[]-=':"
        for i in range (0, len(symbols)):
            word = word.replace(symbols[i],"")
        if len(word) > 0:
            clean_word_list.append(word)
    create_dictionary(clean_word_list)

def create_dictionary(clean_word_list):

    word_count = {}
    for word in clean_word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    #for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
    #    print(key, value)
    #for key in sorted(word_count):
    #    print("%s: %s" % (key, word_count[key]))
    for x, y in sorted(word_count.items(), key = lambda x: x[1], reverse = True):
        print("%s: %s" %(x, y))

start("https://thenewboston.com//forum/category.php?id=10")