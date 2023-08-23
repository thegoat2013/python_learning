'''
Please print out how many times each word in the following paragraph appears.  then print out the word that appears most frequently.

Hint: use a function to split a string to words.

Note: punctuation is not word and should not be counted.
'''

paragraph = "Ethan is a ten years old boy. He is very smart. He loves to read and plays minecraft.   His favoriate actitivy is to assemble robots.  He has a naughty sister but he really cares about her.  He is a good swimmer and will go to tryout for swim team this weekend.  One of the things he likes is that he always beats  his daddy during the night fight."
paragraph = paragraph.split()
dict={}
for word in paragraph:
    for key in dict.keys():
        if word == key:
            dict[word] = dict[word]+1
print(dict)            