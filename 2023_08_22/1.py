'''
Please print out how many times each word in the following paragraph appears.  then print out the word that appears most frequently.

Hint: use a function to split a string to words.

Note: punctuation is not word and should not be counted.
'''

paragraph = "Ethan is a ten years old boy. He is very smart. He loves to read and plays minecraft.   His favoriate actitivy is to assemble robots.  He has a naughty sister but he really cares about her.  He is a good swimmer and will go to tryout for swim team this weekend.  One of the things he likes is that he always beats  his daddy during the night fight."
words = paragraph.split()
dict={}
for word in words:
    if word in dict:
        dict[word] = dict[word]+1
    else:
        dict[word] = 1
print(dict)
max_count=0
max_word=""
for word,count in dict.items():
   if count > max_count:
       max_count=count
       max_word=word
print(max_word)
print(max_count)
            