# //slice to count grab the string between periods
# //count of spaces +1
# //save count to a dictionary of string slice:word count
# //return largest number of the array


sentence = []
words = []

with open('file.txt', encoding="utf8") as file:
    data = file.read().replace('\n', '')
    exclamation = data.replace("!", ".")
    question = exclamation.replace("?", ".")
    ellipses = question.replace("...", ".")
    sentences = (ellipses.split("."))

    y = 0 
    wc_sentence = []
    words_only_list = []
    for x in sentences:
        words = (sentences[y].split(" "))
        words_only = ([d for d in words if d != "" and d != "—" ])
        counts = [len(([d for d in words if d != ""]))]
        words_only_list.append(words_only)
        wc_sentence.append(counts)
        y = y + 1

    longest = max(wc_sentence)
    location = (wc_sentence.index(longest))
    longest_sentence=(words_only_list[location])
    # Function to convert  
    # print(longest_sentence)
    listToStr = ' '.join([str(elem) for elem in longest_sentence])

print(listToStr) 
print('The longest sentence in this fic is ' + str(longest) + ' words long.')
# print((words_only_list[location]))
