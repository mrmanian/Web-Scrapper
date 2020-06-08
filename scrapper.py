from bs4 import BeautifulSoup
from collections import OrderedDict
import urllib.request

words_dict = {}  # Dictionary to store words and their count
alphabets = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
             "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]  # List of capital alphabets A-Z

for x in alphabets:
    for y in alphabets:
        letters = x + y
        website_url = "https://en.wikipedia.org/wiki/" + letters  # Url for Wikipedia entries with two capital letters
        print("Processing page:", website_url)  # Prints that the url is being processed (shows program is looping)
        file = urllib.request.urlopen(website_url)  # Opens page using urllib command
        html = file.read()
        obj_html = BeautifulSoup(html, "html.parser")  # Converts a text from HTML format to text format using BeautifulSoup
        t = obj_html.find(id="bodyContent")
        for element in t(["script", "style"]):  # Removes all script and style elements
            element.extract()
        text = t.get_text()  # Gets text only
        for w in text.split():
            word = w.lower()
            if word in words_dict:  # Increments count by 1 if word already exist in dictionary
                words_dict[word] += 1
            else:
                words_dict[word] = 1  # Add word as a new entry with count 1 if it doesn't already exist

for symbol in "'[@_!#$%^&*()<>?/\\|}{~:]'":  # Get rid of any special characters that may exist in the dictionary
    for k in words_dict.copy():
        if symbol == k:
            del words_dict[k]

final_dict = OrderedDict(sorted(words_dict.items(), key=lambda kv: kv[1]))  # Sorts dictionary
print("\n")
for e in list(reversed(list(final_dict)))[0:15]:  # Prints out last 15 elements in dictionary
    print(" {} {} ".format(final_dict[e], e))
