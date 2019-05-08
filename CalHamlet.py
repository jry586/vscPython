#CalHamlet.py
excludesTxt = open("hamletExcludes.txt").read()
excludes = set(excludesTxt.split(","))
#excludes = {"the","and","of","you","a","i","my","in","to","it","that","is","not","his","this","but","with","for",}
def getText():
    txt = open("hamlet.txt", "rt").read()
    txt = txt.lower()
    for ch in '!"#$%&()*+-,./:;<>=?@[\\]^_`~{}|':
        txt = txt.replace(ch,' ')
    return txt
hamletTxt = getText()
words = hamletTxt.split()
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
for word in excludes:
    del counts[word]
items = list(counts.items())
items.sort(key = lambda x : x[1], reverse = True)
for i in range(10):
    word, count = items[i]
    print("{:>10} : {:<5}".format(word,count))