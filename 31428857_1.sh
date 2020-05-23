#!/bin/bash
# Michael Manian
# CS 288 HW 2 Problem 1

for x in A B C D E F G H I J K L M N O P Q R S T U V W X Y Z; do
  for y in A B C D E F G H I J K L M N O P Q R S T U V W X Y Z; do
    letters=${x}${y}
    wget https://en.wikipedia.org/wiki/${letters} -O ${letters}.html # Gets and downloaded wiki html page
    lynx -dump -nolist ${letters}.html > ${letters}.txt # Remove HTML tags and convert into text file
    grep -oh "[a-zA-Z]*" ${letters}.txt >> allwords.txt # Finds all the words and appends into new file
  done
done

sort -o sorted.txt allwords.txt # Sorts words into new file
uniq -ic sorted.txt final.txt # Counts number of occurences of the words into new file, case insensitive
sort -nr final.txt | head -n 15
# Sort by number of occurrences in reverse order based on number (largest to smallest), prints out first 15 words
