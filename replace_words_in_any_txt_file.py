import re

filename = "filename.txt"

with open(filename, 'r+') as f:
    text = f.read()
    text = re.sub('word_to_be_subbed', 'new_word', text)
    f.seek(0)
    f.write(text)
    f.truncate()
