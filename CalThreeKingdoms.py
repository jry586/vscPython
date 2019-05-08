#CalThreeKingdoms.py
import jieba
import time
start=time.perf_counter()
Fexcludes = open("ThreeKingdomsExcludes.txt",encoding='utf-8-sig')
excludestxt=Fexcludes.read()
Fexcludes.close()
excludes = set(excludestxt.split(sep="，"))
Fthesaurus=open("thesaurus.txt",encoding="utf-8-sig")
Dthesaurus={}
for line in Fthesaurus:
    Lsynonym=line.split("：")
    Dthesaurus[Lsynonym[0]]=Lsynonym[1].replace("\n","").split("，")
Fthesaurus.close()
Ftxt=open("threeKingdoms.txt",encoding='utf-8-sig')
txt=Ftxt.read()
Ftxt.close()
words=jieba.lcut(txt)
counts={}
for word in words:
    if len(word)==1:
        continue
    else:
        for syword in Dthesaurus:
            if word in Dthesaurus[syword]:
                word=syword
        counts[word]=counts.get(word,0)+1
for word in excludes:
    if word!='' and word in counts:
        del counts[word]
# for word in  counts:
#     if word in Dthesaurus:
#         for syword in Dthesaurus[word]:
#             counts[word] +=counts[syword]
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
print("《三国演义》中出现次数最多的10个人物为：")
for i in range(10):
    word,count = items[i]
    print("{0:<3}：出现{1:<4}次".format(word,count))
print("用时：{}".format(time.perf_counter()-start))