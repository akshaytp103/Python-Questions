# Reverse the string by line
def process(paragraphs):
    lines = paragraphs.split('.')
    for i, line in enumerate(lines):
        x = line.split()
        x.reverse()
        lines[i] = x

# find palindrom and non palindrom 

    for line in lines:
        for i, word in enumerate(line):
            if '#' in word:
                x = list(word)
                ind = word.index('#')
                x[ind] = x[len(word) - (ind + 1)]
                if x == x[::-1]:
                    line[i] = str(''.join(x))   
                else:
                    line[i] = word.replace(word, len(word) * '@')

# join the paragraph 

    for i, line in enumerate(lines):
        lines[i] = ' '.join(line)       
    lines = '. '.join(lines)
    print('Required output =\n',lines)


paragraph = "mal#yalam is our mother tong#e." \
            " It is a langua#e spo#en in the Indian state of kerala." \
            "m#dam ha#nah teaches Malayalam." \
            "neve# is a #tudent of hannah."

process(paragraph)

